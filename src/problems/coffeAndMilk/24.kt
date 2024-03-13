package problems.coffeAndMilk

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val n = reader.nextInt()
  val out = when {
    n <= 0 -> "E"
    n <= 35 -> "D"
    n <= 60 -> "C"
    n <= 85 -> "B"
    else -> "A"
  }
  println(out)
}