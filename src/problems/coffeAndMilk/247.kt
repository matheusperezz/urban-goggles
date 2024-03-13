package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val list = mutableListOf<Int>()

  val n = reader.nextInt()
  for (i in 0 until n){
    val p = reader.nextInt()
    val m = reader.nextInt()
    list.add(p+m)
  }

  list.forEach {
    println(it)
  }
}