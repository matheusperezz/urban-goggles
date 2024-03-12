package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val n1 = reader.nextFloat()
  val n2 = reader.nextFloat()
  val n3 = reader.nextFloat()

  val result = ((n1*4) + (n2*4) + (n3*2)) / 10
  println("%.2f".format(result))
}