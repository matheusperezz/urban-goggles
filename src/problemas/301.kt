package problemas

import java.util.Scanner

fun main() {
    val reader = Scanner(System.`in`)

    val firstline = reader.nextLine().split(" ")
    val secondline = reader.nextLine().split(" ")

    val z = firstline[0][0]
    val g = firstline[1][0]
    val d = secondline[0][0]
    val c = secondline[1][0]

    if (z == d){
        println("Bloqueado")
        return
    } else {
        println("Driblado")
        if (g == c){
            println("...e o goleiro pega")
        } else {
            println("Gol")
        }
    }
}
