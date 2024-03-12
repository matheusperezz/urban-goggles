package problems.base

import java.lang.String.format
import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val (op, x, y) = reader.nextLine().split(" ")
  val n1 = x.toInt()
  val n2 = y.toInt()

  when(op){
    "+" -> println(n1+n2)
    "-" -> println(n1-n2)
    "/" -> println(format("%.1f", n1.toFloat()/n2.toFloat()))
    "*" -> println(n1*n2)
  }
}
