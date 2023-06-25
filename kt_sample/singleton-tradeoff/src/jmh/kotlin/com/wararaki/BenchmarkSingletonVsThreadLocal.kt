package com.wararaki

import SystemComponentSingletonDoubleCheckedLocking
import SystemComponentSingletonSynchronized
import SystemComponentThreadLocal
import org.openjdk.jmh.annotations.*
import org.openjdk.jmh.infra.Blackhole
import java.util.concurrent.TimeUnit

@Fork(1)
@Warmup(iterations=1)
@Measurement(iterations=1)
@BenchmarkMode(Mode.AverageTime)
@Threads(100)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
open class BenchmarkSingletonVsThreadLocal {
    companion object {
        private const val NUMBER_OF_ITERATIONS = 50000
    }

    @Benchmark
    fun singletonWithSynchronization(blackhole: Blackhole) {
        for (i in 0 until NUMBER_OF_ITERATIONS) {
            blackhole.consume(SystemComponentSingletonSynchronized.getInstance())
        }
    }

    @Benchmark
    fun singletonWithDoubleCheckedLocking(blackhole: Blackhole) {
        for (i in 0 until NUMBER_OF_ITERATIONS) {
            blackhole.consume(SystemComponentSingletonDoubleCheckedLocking.getInstance())
        }
    }

    @Benchmark
    fun singletonWithThreadLocal(blackhole: Blackhole) {
        for (i in 0 until NUMBER_OF_ITERATIONS) {
            blackhole.consume(SystemComponentThreadLocal.get())
        }
    }
}