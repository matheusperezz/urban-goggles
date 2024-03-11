package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val p = reader.nextInt()
  val r = reader.nextInt()
  if (p + r == 2){
    println("A")
  } else {
    if (p == 0){
      println("C")
    } else {
      println("B")
    }
  }
}
