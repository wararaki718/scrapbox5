package com.wararaki.opensearch_spring.model

import org.springframework.data.elasticsearch.annotations.Field
import org.springframework.data.elasticsearch.annotations.FieldType

data class Author (
    @Field(type = FieldType.Text) val name: String,
){
}
