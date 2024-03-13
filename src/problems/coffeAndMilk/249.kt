package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val a = reader.nextInt()
  val b = reader.nextInt()
  val c = reader.nextInt()

  if (a == b && b != c) {
    println("C")
  } else if (a == c && c != b) {
    println("B")
  } else if (b == c && c != a) {
    println("A")
  } else {
    println("Empate")
  }
}