import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class SystemComponentTest {

    @Test
    fun publicApiMethod() {
        val systemComponent = SystemComponent()
        val result = systemComponent.publicApiMethod()
        assertEquals(result, 0)
    }
}