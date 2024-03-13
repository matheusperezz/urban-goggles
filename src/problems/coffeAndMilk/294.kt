package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val n = reader.nextInt()
  for (i in 0 until 101){
    println(i*n)
  }
}