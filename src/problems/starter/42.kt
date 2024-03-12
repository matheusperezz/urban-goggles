package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val list = mutableListOf<Int>()
  while (true){
    val (n, c, d) = reader.nextLine().split(" ").map { i -> i.toInt() }
    if (n == 0 && c == 0 && d == 0){
      break
    }
    list.add(n*c*d)
  }

  list.forEach {
    println(it)
  }
}