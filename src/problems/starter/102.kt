package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val list = mutableListOf<Int>()
  while (true){
    val n = reader.nextInt()
    if (n == 0) {
      break
    }
    // inline solution: list.add(n*-1)
    list.add(n)
  }
  val output = list.map { i -> i*-1 }
  output.forEach { println(it) }
}
