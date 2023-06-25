class SystemComponentThreadLocal {
    companion object {
        private var threadLocalValue: ThreadLocal<SystemComponent> = ThreadLocal.withInitial{SystemComponent()}

        public fun set() {
            threadLocalValue.set(SystemComponent())
        }

        public fun executeAction() {
            val systemComponent = threadLocalValue.get()
        }

        public fun get(): SystemComponent {
            return threadLocalValue.get();
        }
    }
}