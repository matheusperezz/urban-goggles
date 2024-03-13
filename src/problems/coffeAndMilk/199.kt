package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val n = reader.nextInt()
  val xp = reader.nextInt()
  val yoda = reader.nextInt()
  val luke = reader.nextInt()
  val ahsoka = reader.nextInt()

  val total = n * xp
  println("""
    Yoda ${total+yoda}
    Luke ${total+luke}
    Ahsoka ${total+ahsoka}
  """.trimIndent())
}