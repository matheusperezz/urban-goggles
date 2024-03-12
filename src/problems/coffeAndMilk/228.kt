package problems.coffeAndMilk

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val x = reader.nextFloat()
  val y = reader.nextFloat()
  println("%.2f".format(x+y))
}
