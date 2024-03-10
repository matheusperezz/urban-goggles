package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val firstline = reader.nextLine().split(" ")
  val n1 = firstline[0].toInt()
  val n2 = firstline[1].toInt()

  println(n1 + n2)
}
