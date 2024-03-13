package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val list = mutableListOf<Long>()
  for (i in 0 until 5){
    list.add(reader.nextLong())
  }
  println(list.sum())
}