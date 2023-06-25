class SystemComponentSingletonDoubleCheckedLocking {
    companion object {
        @Volatile
        private var instance: SystemComponent? = null

        public fun getInstance(): SystemComponent? {
            if (instance == null) {
                synchronized(ThreadSafeSingleton.javaClass) {
                    if (instance == null) {
                        instance = SystemComponent()
                    }
                }
            }
            return instance
        }
    }
}