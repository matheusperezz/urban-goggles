package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val list = mutableListOf<Int>()
  for (i in 0 until 6){
    list.add(reader.nextInt())
  }

  var l = 0
  var p = 0

  list.forEachIndexed { i, v ->
    if (i % 2 == 0){
      l += v
    } else {
      p += v
    }
  }

  when {
    l > p -> println("Lucas")
    p > l -> println("Pedro")
    else -> println("Empate")
  }
}