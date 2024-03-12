package problems.base

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val type = reader.nextLine()
  val ds = reader.nextDouble()
  val dm = reader.nextDouble()
  val dh = reader.nextDouble()
  var counter = 0
  var laps = 0.0

  val tire: Double = when(type) {
    "S" -> ds
    "M" -> dm
    else -> dh
  }

  while (laps <= 80.0 - tire){
    counter++
    laps += tire
  }
  println(counter)
}
