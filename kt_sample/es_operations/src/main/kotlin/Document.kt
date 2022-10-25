import kotlinx.serialization.Serializable

@Serializable
data class Document (
    val id: String,
    val name: String,
    val tags: List<String>) {}
