data class Message(val description: String)

fun main() {

    val message = Message("Renzo")
    print("Hello ${message.description}")
}