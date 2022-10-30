package com.wararaki.elasticsearch.springboot.model

import org.springframework.data.annotation.Id
import org.springframework.data.elasticsearch.annotations.*
import org.springframework.data.elasticsearch.annotations.FieldType

@Document(indexName = "blog")
data class Article (
    @Id val id: String,
    @MultiField(mainField = Field(type = FieldType.Text, fielddata = true), otherFields = [InnerField(suffix = "verbatim", type = FieldType.Keyword)])  val title: String,
    @Field(type = FieldType.Nested, includeInParent = true) val authors: List<Author>,
    @Field(type = FieldType.Keyword) val tags: List<String>
    ) {
}
