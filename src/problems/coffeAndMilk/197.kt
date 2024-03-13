package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val s = reader.nextLine()

  when(s){
    "idoso" -> println("gratuidade")
    "estudante" -> println("10 reais")
    "casadinha" -> println("30 reais")
    "trio" -> println("40 reais")
    else -> println("20 reais")
  }
}