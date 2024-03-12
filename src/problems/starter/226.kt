package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  var n = reader.nextLine().toInt()
  val s = reader.nextLine()
  while (n > 0){
    println("$n. $s")
    n--
  }
}
