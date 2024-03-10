package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val line = reader.nextLine().split(" ")
  val part = line[0]

  val s = line.subList(1,6).map { i -> i.toDouble() }
  val result = (s.sum()/5)

  println("$part %.1f".format(result))
}