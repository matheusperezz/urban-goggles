package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val list = mutableListOf<Int>()
  for (i in 0 until 6){
    list.add(reader.nextInt())
  }

  val total = list.sum()
  when {
    total < 40 -> println("B-")
    total < 60 -> println("B")
    total < 80 -> println("B+")
    total < 100 -> println("A-")
    total < 150 -> println("A")
    total < 180 -> println("A+")
    total < 200 -> println("S-")
    total < 250 -> println("S")
    else -> println("S+")
  }
}