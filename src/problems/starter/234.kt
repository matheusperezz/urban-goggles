package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val bMax = reader.nextInt().toFloat()
  val bMin = reader.nextInt().toFloat()
  val h = reader.nextInt().toFloat()

  val area = ((bMax + bMin) * h) / 2

  println("A=$area")
}