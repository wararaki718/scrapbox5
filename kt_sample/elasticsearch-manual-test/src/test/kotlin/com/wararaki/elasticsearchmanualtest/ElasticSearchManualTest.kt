package com.wararaki.elasticsearchmanualtest

import org.elasticsearch.action.DocWriteResponse.Result
import org.elasticsearch.action.delete.DeleteRequest
import org.elasticsearch.action.get.GetRequest
import org.elasticsearch.action.index.IndexRequest
import org.elasticsearch.action.search.SearchRequest
import org.elasticsearch.client.RequestOptions
import org.elasticsearch.client.RestHighLevelClient
import org.elasticsearch.xcontent.XContentType
import org.junit.jupiter.api.BeforeAll
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.TestInstance
import org.springframework.data.elasticsearch.client.ClientConfiguration
import org.springframework.data.elasticsearch.client.RestClients
import kotlin.test.assertEquals
import com.google.gson.Gson
import org.elasticsearch.action.search.SearchType
import org.elasticsearch.index.query.QueryBuilders
import org.elasticsearch.search.builder.SearchSourceBuilder
import org.elasticsearch.xcontent.XContentFactory

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class ElasticSearchManualTest {
    private val persons: MutableList<Person> = mutableListOf()
    private var client: RestHighLevelClient? = null

    @BeforeAll
    fun setUp() {
        val person1 = Person(10, "John Doe", "2000")
        val person2 = Person(20, "Janette Doe", "2020")

        persons.add(person1)
        persons.add(person2)

        val clientConfiguration: ClientConfiguration = ClientConfiguration.builder().connectedTo("localhost:9200").build()
        client = RestClients.create(clientConfiguration).rest()
    }

    @Test
    fun sampleTest() {
        val json = "{\"age\":20,\"dateOfBirth\":1471466076564,\"fullName\":\"John Doe\"}"
        val request = IndexRequest("people")

        request.source(json, XContentType.JSON)

        val response = client?.index(request, RequestOptions.DEFAULT)
        val index = response?.index
        val version = response?.version

        assertEquals(1, version)
        assertEquals("people", index)
    }

    @Test
    fun testIndexOperations() {
        val json = "{\"age\":10,\"dateOfBirth\":1471455886564,\"fullName\":\"Johan Doe\"}"
        val request = IndexRequest("people")
        request.source(json, XContentType.JSON)

        val response = client?.index(request, RequestOptions.DEFAULT)
        val id = response?.id

        val getRequest = GetRequest("people")
        getRequest.id(id)

        val getResponse = client?.get(getRequest, RequestOptions.DEFAULT)
        println(getResponse?.sourceAsString)

        val deleteRequest = DeleteRequest("people")
        deleteRequest.id(id)

        val deleteResponse = client?.delete(deleteRequest, RequestOptions.DEFAULT)

        assertEquals(Result.DELETED, deleteResponse?.result)
    }

    @Test
    fun testMatchAll() {
        val request = SearchRequest()
        val response = client?.search(request, RequestOptions.DEFAULT)
        val hits = response?.hits?.hits
        val results = hits?.map { hit ->  Gson().fromJson(hit?.sourceAsString, Person::class.java)}
        results?.forEach { println(it) }
    }

    @Test
    fun testQuery() {
        val ageBuilder = SearchSourceBuilder().postFilter(QueryBuilders.rangeQuery("age").from(5).to(15))
        val request = SearchRequest()
        request.searchType(SearchType.DFS_QUERY_THEN_FETCH)
        request.source(ageBuilder)
        val response = client?.search(request, RequestOptions.DEFAULT)

        val nameBuilder = SearchSourceBuilder().postFilter(QueryBuilders.simpleQueryStringQuery("+John -Doe OR Janette"))
        val request2 = SearchRequest()
        request2.searchType(SearchType.DFS_QUERY_THEN_FETCH)
        request2.source(nameBuilder)
        val response2 = client?.search(request2, RequestOptions.DEFAULT)

        val matchBuilder = SearchSourceBuilder().postFilter(QueryBuilders.matchQuery("John", "Name*"))
        val request3 = SearchRequest()
        request3.searchType(SearchType.DFS_QUERY_THEN_FETCH)
        request3.source(matchBuilder)

        val response3 = client?.search(request3, RequestOptions.DEFAULT)

        response?.hits?.hits?.map { hit -> Gson().fromJson(hit?.sourceAsString, Person::class.java)}?.forEach {println(it)}
        response2?.hits?.hits?.map { hit -> Gson().fromJson(hit?.sourceAsString, Person::class.java)}?.forEach {println(it)}
        response3?.hits?.hits?.map { hit -> Gson().fromJson(hit?.sourceAsString, Person::class.java)}?.forEach {println(it)}
    }

    @Test
    fun testBuilderHelper() {
        val builder = XContentFactory.jsonBuilder()
            .startObject()
            .field("fullName", "Test")
            .field("salary", "11500")
            .field("age", "10")
            .endObject()

        val request = IndexRequest("people")
        request.source(builder)

        val response = client?.index(request, RequestOptions.DEFAULT)

        assertEquals(Result.CREATED, response?.result)
    }
}