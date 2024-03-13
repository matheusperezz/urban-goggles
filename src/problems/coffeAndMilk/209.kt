package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val n = reader.nextInt()
  var total = 0
  for (i in 0 until n){
    val x = reader.nextInt()
    total += x
  }
  println(total)
}