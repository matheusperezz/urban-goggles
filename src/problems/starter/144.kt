package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val n = reader.nextInt()
  val s = if (n%42==0) "Sim" else "Nao"
  println(s)
}
