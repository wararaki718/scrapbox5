class SystemComponentSingletonSynchronized {
    companion object {
        private var instance: SystemComponent? = null

        @Synchronized
        public fun getInstance(): SystemComponent? {
            if (instance == null) {
                instance = SystemComponent()
            }
            return instance
        }
    }
}