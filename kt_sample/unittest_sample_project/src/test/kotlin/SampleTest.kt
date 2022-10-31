import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

internal class SampleTest {
    private val testSample: Sample = Sample()

    @Test
    fun testSum() {
        val expected = 42
        assertEquals(expected, testSample.sum(40, 2))
    }

    @Test
    fun testSum2() {
        assertEquals(10, testSample.sum(8, 2))
    }
}