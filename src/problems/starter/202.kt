package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  var total = 0
  for (i in 0 until 5){
    val i = reader.nextLine().toInt()
    total += i
  }
  if (total <= 5000){
    println("Acesso liberado")
  } else {
    println("Acesso proibido")
  }
}