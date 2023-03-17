package gradleexample;

class KotlinApp {

    public fun getGreeting() : String {
        return "Hello World in Kotlin";
    }
}

fun main() {
    println(KotlinApp().getGreeting())
}