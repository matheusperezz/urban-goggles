package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val tr = reader.nextInt()
  val i = reader.nextInt()
  val tn = reader.nextInt()

  if (tn == 2){
    println("VITORIA")
  } else {
    println("${9-tr} ${3-i} ${2-tn}")
  }
}