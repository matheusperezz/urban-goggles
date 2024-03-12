package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val n = reader.nextInt() // 10
  var total = 1
  for (i in 1 until n+1){
    total *= 2
  }
  println(total)
}
