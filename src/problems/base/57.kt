package problems.base

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val n = reader.nextInt()
  val list = mutableListOf<Int>()
  val out = mutableListOf<Int>()
  for (i in 0 until n){
    list.add(reader.nextInt())
  }

  list.forEachIndexed { i, v ->
    if (i == 0 && i < n-1){
      val next = list[i+1]
      out.add(v+next)
    } else if (i == n-1){
      val prev = list[i-1]
      out.add(prev+v)
    } else {
      val prev = list[i-1]
      val next = list[i+1]
      out.add(prev+v+next)
    }
  }

  out.forEach {
    println(it)
  }
}