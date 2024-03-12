package problems.base

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val arrSize = reader.nextInt()
  val list = mutableListOf<Int>()

  for (i in 0 until arrSize){
    list.add(0, reader.nextInt())
  }

  list.forEach {
    print("$it ")
  }
  println()
}
