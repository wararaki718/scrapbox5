class SystemComponent {
    fun publicApiMethod(): Int {
        return privateApiMethod()
    }

    private fun privateApiMethod(): Int {
        return complexCalculations()
    }

    private fun complexCalculations(): Int {
        return 0
    }
}
