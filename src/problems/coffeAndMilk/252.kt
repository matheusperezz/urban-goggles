package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val x1 = reader.nextInt()
  val y1 = reader.nextInt()
  val x2 = reader.nextInt()
  val y2 = reader.nextInt()

  if (x1 == x2 && y1 == y2){
    println("Soltar pacote")
  } else {
    println("Nao soltar pacote")
  }
}