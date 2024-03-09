package problems.legend

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val n = reader.nextInt()
  reader.nextLine()
  val list = mutableListOf<String>()
  val occr = HashMap<String, Int>()

  for (i in 0 until n){
    val words = reader.nextLine().split(" ")
    for (w in words){
      val count = occr[w]
      if (count == null){
        occr[w] = 1
      } else {
        occr[w] = count + 1
      }
    }
  }

  occr.forEach { (k, v) ->
    if (v == 1){
      list.add(k)
    }
  }

  println(list.size)
  for (w in list.sorted()){
    println(w)
  }
}
