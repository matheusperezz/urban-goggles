package problems.coffeAndMilk

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val x = reader.nextInt()

  if (x < 0) {
    println(-1 * x)
  } else {
    println(x)
  }
}