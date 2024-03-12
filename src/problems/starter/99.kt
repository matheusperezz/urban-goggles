package problems.starter

import java.lang.String.format
import java.util.*

fun main() {
  val reader = Scanner(System.`in`)
  val mph = reader.nextFloat()
  val kmh = mph / 0.62137
  println(format("%.2f", kmh))
}