package problems.base

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val n = reader.nextInt()
  val s = n % 60
  val m = (n / 60) % 60
  val h = n / 3600

  println("${h}h ${m}m ${s}s")
}
