import org.apache.http.HttpHost
import org.opensearch.action.admin.indices.delete.DeleteIndexRequest
import org.opensearch.action.delete.DeleteRequest
import org.opensearch.action.get.GetRequest
import org.opensearch.action.index.IndexRequest
import org.opensearch.client.RequestOptions
import org.opensearch.client.RestClient
import org.opensearch.client.RestHighLevelClient
import org.opensearch.client.indices.CreateIndexRequest
import org.opensearch.common.settings.Settings


fun main(args: Array<String>) {
    val indexName = "kotlin-test-index"

    val builder = RestClient.builder(HttpHost("localhost", 9200, "http"))
    val client = RestHighLevelClient(builder)

    val createIndexRequest = CreateIndexRequest(indexName)
    createIndexRequest.settings(
        Settings.builder().put("index.number_of_shards", 4).put("index.number_of_replicas", 3)
    )

    val typeMapping = mapOf("type" to "integer")
    val ageMapping = mapOf("age" to typeMapping)
    val mapping = mapOf("properties" to ageMapping)
    createIndexRequest.mapping(mapping)
    val createIndexResponse = client.indices().create(createIndexRequest, RequestOptions.DEFAULT)
    println("create index")
    println(createIndexResponse)

    val request = IndexRequest(indexName)
    request.id("1")

    val stringMapping = mapOf("message:" to "Testing Java REST client")
    request.source(stringMapping)
    val indexResponse = client.index(request, RequestOptions.DEFAULT)
    print("index response")
    println(indexResponse)

    val getRequest = GetRequest(indexName, "1")
    val response = client.get(getRequest, RequestOptions.DEFAULT)
    println(response.sourceAsString)

    val deleteDocumentRequest = DeleteRequest(indexName, "1")
    val deleteResponse = client.delete(deleteDocumentRequest, RequestOptions.DEFAULT)
    println("delete document")
    println(deleteResponse)

    val deleteIndexRequest = DeleteIndexRequest(indexName)
    val deleteIndexResponse = client.indices().delete(deleteIndexRequest, RequestOptions.DEFAULT)
    println("delete index")
    println(deleteIndexResponse)

    client.close()

    println("DONE")
}