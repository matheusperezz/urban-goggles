package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val (a, b) = reader.nextLine().split(" ")
  val dir = "direita"

  if (a == dir){
    if (b == dir){
      println("Tente novamente")
    } else {
      println("Achou")
    }
  } else {
    if (b == dir){
      println("Tente novamente")
    } else {
      println("Morreu")
    }
  }
}