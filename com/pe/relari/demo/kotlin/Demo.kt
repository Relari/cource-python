data class Message(val description: String = "World!")

fun main() {

    val message = Message("Renzo")
    println("Hello ${message.description}")

    val message2 = Message()
    println(sayHello(message2.description))

}

fun sayHello(name: String) = "Hello $name"