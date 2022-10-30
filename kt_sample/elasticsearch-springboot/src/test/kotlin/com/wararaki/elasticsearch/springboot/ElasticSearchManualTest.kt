package com.wararaki.elasticsearch.springboot

import com.wararaki.elasticsearch.springboot.config.Config
import com.wararaki.elasticsearch.springboot.model.Article
import com.wararaki.elasticsearch.springboot.model.Author
import com.wararaki.elasticsearch.springboot.repository.ArticleRepository
import org.junit.After
import org.junit.Before
import org.junit.jupiter.api.Test
import org.junit.runner.RunWith
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.data.elasticsearch.client.elc.ElasticsearchTemplate
import org.springframework.test.context.ContextConfiguration
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner
import kotlin.test.assertNotNull

@RunWith(SpringJUnit4ClassRunner::class)
@ContextConfiguration(classes = [Config::class])
class ElasticSearchManualTest {
    @Autowired
    private lateinit var elasticsearchTemplate: ElasticsearchTemplate

    @Autowired
    private lateinit var articleRepository: ArticleRepository

    private val author1: Author = Author("John Smith")
    private val author2: Author = Author("John Doe")

    @Before
    fun before() {
        val article1: Article = Article(
            "1",
            "Spring Data Elasticsearch",
            listOf(author1, author2),
            listOf("elasticsearch", "spring data")
        )
        articleRepository.save(article1)

        val article2: Article = Article(
            "2",
            "Search Engines",
            listOf(author2),
            listOf("search engine", "tutorial")
        )
        articleRepository.save(article2)

        val article3: Article = Article(
            "3",
            "Second Article About Elasticsearch",
            listOf(author1),
            listOf("elasticsearch", "spring data")
        )
        articleRepository.save(article3)

        val article4: Article = Article(
            "4",
            "Elasticsearch Tutorial",
            listOf(author2),
            listOf("elasticsearch")
        )
        articleRepository.save(article4)
    }

    @After
    fun after() {
        articleRepository.deleteAll()
    }

    @Test
    fun givenArticleService_whenSaveArticle_thenIdIsAssigned() {
        val authors: List<Author> = listOf(author1, author2)

        val article = Article(
            "5",
            "Making Search Elastic",
            authors,
            listOf()
        )

        val result = articleRepository.save(article)
        assertNotNull(result.id)
    }
}