package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val a = reader.nextInt()
  val b = reader.nextInt()
  val c = reader.nextInt()
  val d = reader.nextInt()
  val e = reader.nextInt()
  val f = reader.nextInt()

  val result = ((a+b)*(c-d)*(e+f)) / 2.0
  println("Eu sou FERA nas continhas e o resultado é %.1f".format(result))
}
