package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val a = reader.nextInt()
  val b = reader.nextInt()
  val c = reader.nextInt()

  val output = maxOf(a, b, c)
  println(output)
}