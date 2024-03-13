package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  var n = reader.nextInt()
  when {
    n <= 20 -> println(0)
    else -> {
      n -= 20
      println(n/5)
    }
  }
}