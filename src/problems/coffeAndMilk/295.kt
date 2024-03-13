package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val x = reader.nextInt()
  val list = mutableListOf<Int>()
  for (i in 0 until x){
    list.add(reader.nextInt())
  }
  val y = reader.nextInt()
  list.forEach {
    print("${it*y} ")
  }
  println()
}