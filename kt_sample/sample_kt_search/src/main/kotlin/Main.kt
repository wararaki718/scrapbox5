import com.jillesvangurp.ktsearch.KtorRestClient
import com.jillesvangurp.ktsearch.SearchClient
import com.jillesvangurp.ktsearch.clusterHealth
import com.jillesvangurp.ktsearch.root
import kotlinx.coroutines.runBlocking


fun main(args: Array<String>) {
    val client = SearchClient()

    runBlocking {
        client.root().let {
            resp -> println("${resp.variantInfo.variant}: ${resp.version.number}")
        }
        client.clusterHealth().let {
            resp -> println(resp.clusterName + " is " + resp.status)
        }
    }

    var client2 = SearchClient(
        KtorRestClient(
            "localhost",
            9200
        )
    )
    runBlocking {
        client2.root().let {
                resp -> println("${resp.variantInfo.variant}: ${resp.version.number}")
        }
        client2.clusterHealth().let {
                resp -> println(resp.clusterName + " is " + resp.status)
        }
    }

    println("DONE!")
}