package problems.legend

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val n = reader.nextInt()
  reader.nextLine()

  val hmap = HashMap<String, Int>()

  for (i in 0 until n){
    val (star, _, population) = reader.nextLine().split(" ")
    val intpop = population.toInt()

    val count = hmap[star]
    if (count == null){
      hmap[star] = intpop
    } else {
      if (intpop > count){
        hmap[star] = intpop
      }
    }

  }

  val maxCombination = hmap.maxBy { entry -> entry.value }
  println("${maxCombination.key} ${maxCombination.value}")

  val sortedHmap = hmap.toSortedMap()
  sortedHmap.forEach { (k, v) ->
    println("$k $v")
  }
}
