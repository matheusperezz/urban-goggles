package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val n = reader.nextInt()
  if (n % 7 == 0){
    println("É MULTIPLO DE 7")
  } else {
    println("ESSE NÃO É")
  }
}