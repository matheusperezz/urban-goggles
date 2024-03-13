package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  var total = 0
  for (i in 0 until 5){
    val n = reader.nextInt()
    if (i == 0){
      total = n
    } else {
      total -= n
    }
  }
  println(total)
}