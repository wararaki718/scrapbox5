class ThreadSafeSingleton {
    companion object {
        private var instance: ThreadSafeSingleton? = null

        @Synchronized
        public fun getInstance(): ThreadSafeSingleton? {
            if (instance == null) {
                instance = ThreadSafeSingleton()
            }
            return instance
        }
    }
}
