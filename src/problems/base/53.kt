package problems.base

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)

  val l1 = mutableListOf<Int>()
  val l2 = mutableListOf<Int>()

  val n = reader.nextInt()
  for (i in 0 until n){
    l1.add(reader.nextInt())
  }

  val m = reader.nextInt()
  for (i in 0 until m){
    l2.add(reader.nextInt())
  }

  l1.removeIf { i -> l2.contains(i) }
  l1.forEach {
    print("$it ")
  }
  println()
}