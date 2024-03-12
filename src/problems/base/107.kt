package problems.base

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val n = reader.nextInt()
  val list = mutableListOf<Int>()
  for (i in 0 until n){
    list.add(reader.nextInt())
  }
  var output = 1
  var prev = list[0]
  val r = mutableListOf<Int>()
  list.forEach { curr ->
    if (curr > prev){
      output++
    } else {
      output = 1
    }
    r.add(output)
    prev = curr
  }
  println(r.max())
}
