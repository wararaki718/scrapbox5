package com.wararaki.elasticsearchmanualtest

import org.elasticsearch.action.index.IndexRequest
import org.elasticsearch.client.RequestOptions
import org.elasticsearch.client.RestHighLevelClient
import org.elasticsearch.xcontent.XContentType
import org.junit.jupiter.api.BeforeAll
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.TestInstance
import org.springframework.data.elasticsearch.client.ClientConfiguration
import org.springframework.data.elasticsearch.client.RestClients
import kotlin.test.assertEquals

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class ElasticSearchManualTest {
    private val persons: MutableList<Person> = mutableListOf()
    private var client: RestHighLevelClient? = null

    @BeforeAll
    fun setUp() {
        val person1 = Person(10, "hello", "2000")
        val person2 = Person(20, "world", "2020")

        persons.add(person1)
        persons.add(person2)

        val clientConfiguration: ClientConfiguration = ClientConfiguration.builder().connectedTo("localhost:9200").build()
        client = RestClients.create(clientConfiguration).rest()
    }

    @Test
    fun sample_test() {
        val json = "{\"age\":20,\"dateOfBirth\":1471466076564,\"fullName\":\"John Doe\"}"
        val request = IndexRequest("people")

        request.source(json, XContentType.JSON)

        val response = client?.index(request, RequestOptions.DEFAULT)
        val index = response?.index
        val version = response?.version

        assertEquals(1, version)
        assertEquals("people", index)
    }
}