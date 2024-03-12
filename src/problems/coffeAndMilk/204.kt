package problems.coffeAndMilk

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val e = reader.nextInt()
  val t = reader.nextInt()
  val v = e / t
  println(v)
}