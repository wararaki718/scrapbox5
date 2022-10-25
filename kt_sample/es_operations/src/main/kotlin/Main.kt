import com.jillesvangurp.ktsearch.*
import com.jillesvangurp.searchdsls.querydsl.bool
import com.jillesvangurp.searchdsls.querydsl.matchPhrasePrefix
import com.jillesvangurp.searchdsls.querydsl.term
import kotlinx.coroutines.runBlocking

fun main(args: Array<String>) {
    val client = SearchClient(
        KtorRestClient("127.0.0.1", 9200)
    )

    runBlocking {
        client.root().let {
            response -> println("${response.variantInfo.variant}: ${response.version.number}")
        }
        client.clusterHealth().let {
            response -> println(response.clusterName + " is " + response.status)
        }
    }

    val firstIndexName = "my-first-index"
    val json = """{"message": "hello, world."}"""
    runBlocking {
        // create index
        client.createIndex(firstIndexName)
        client.indexDocument(firstIndexName, json)
        println(client.getIndex(firstIndexName).keys)

        // delete index
        client.deleteIndex(firstIndexName)
    }

    val docIndexName = "docs-search"
    runBlocking {
        //client.deleteIndex(docIndexName)
        client.createIndex(docIndexName) {
            mappings { text(Document::id) }
            mappings { text(Document::name) }
            mappings { keyword(Document::tags) }
        }
    }

    val docs = listOf(
        Document(
            id = "1",
            name = "Apple",
            tags = listOf("fruit")
        ),
        Document(
            id = "2",
            name = "Banana",
            tags = listOf("fruit")
        ),
        Document(
            id = "3",
            name = "Beans",
            tags = listOf("legumes")
        )
    )

    docs.forEach { doc ->
        runBlocking {
            client.indexDocument(
                target = docIndexName,
                document = doc,
                id = doc.id,
                refresh = Refresh.WaitFor
            )
        }
    }

    runBlocking {
        println(client.search(docIndexName).ids)
    }

    // use query
    val searchQuery = """
        {
            "query": {
                "term": {
                    "tags": {
                        "value": "legumes"
                    }
                }
            }
        }
    """.trimIndent()
    runBlocking {
        println(client.search(docIndexName, rawJson=searchQuery))
    }

    // parse results
    runBlocking {
        val results = client.search(docIndexName) {
            from = 0
            resultSize = 100
            trackTotalHits = "true"
            query = bool {
                filter(
                    term(Document::tags, "fruit")
                )
                should(
                    matchPhrasePrefix(Document::name, "ban")
                )
            }
        }.parseHits<Document>().map { it?.name }
        println(results)
    }

    runBlocking {
        client.deleteIndex(docIndexName)
    }

    println("DONE")
}