package com.wararaki.elasticsearch.springboot.model

import org.springframework.data.elasticsearch.annotations.Field
import org.springframework.data.elasticsearch.annotations.FieldType

data class Author (
    @Field(type = FieldType.Text) val name: String,
        ){
}
