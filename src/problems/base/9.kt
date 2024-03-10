package problems.base

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val (a, b, c) = reader.nextLine()!!.split(" ").map { i -> i.toInt() }
  val (x, y, z) = reader.nextLine()!!.split(" ").map { i -> i.toInt() }

  val l = (x / a).toLong()
  val h = (y / b).toLong()
  val p = (z / c).toLong()

  val res: Long = l * h * p
  println(res)
}
