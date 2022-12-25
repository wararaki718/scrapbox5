package com.wararaki.opensearch_spring.repository

import com.wararaki.opensearch_spring.model.Article
import org.springframework.data.elasticsearch.annotations.Query
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository
import org.springframework.stereotype.Repository
import java.awt.print.Pageable

@Repository
interface ArticleRepository: ElasticsearchRepository<Article, String>{
    fun findByAuthorsName(name: String, pageable: Pageable)

    @Query("{\"bool\": {\"must\": [{\"match\": {\"authors.name\": \"?0\"}}]}}")
    fun findByAuthorsNameUsingCustomQuery(name: String, pageable: Pageable)

    @Query("{\"bool\": {\"must\": {\"match_all\": {}}, \"filter\": {\"term\": {\"tags\": \"?0\" }}}}")
    fun findByFilteredTagQuery(tag: String, pageable: Pageable)

    @Query("{\"bool\": {\"must\": {\"match\": {\"authors.name\": \"?0\"}}, \"filter\": {\"term\": {\"tags\": \"?1\" }}}}")
    fun findByAuthorsNameAndFilteredTagQuery(name: String, tag: String, pageable: Pageable)
}
