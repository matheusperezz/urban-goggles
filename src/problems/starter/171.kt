package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  var counter = 0
  while (true){
    val input = reader.nextInt()
    if (input == 0){
      break
    }
    counter += input
  }

  println(counter)
}
