package com.wararaki.elasticsearch.springboot

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class ElasticsearchSpringbootApplication

fun main(args: Array<String>) {
	runApplication<ElasticsearchSpringbootApplication>(*args)
}
