import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

internal class CalculatorTest {
    @Test
    fun testMultiply2By2() {
        val calculator = Calculator()
        val result = calculator.parse("2 * 2")
        assertEquals(4, result)
    }

    @Test
    internal fun testDivide2By2() {
        val calculator = Calculator()
        val result = calculator.parse("2 / 2")
        assertEquals(1, result)
    }
}