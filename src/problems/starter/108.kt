package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val n = reader.nextInt()
  val list = mutableListOf<Int>()
  for (i in 0 until n){
    list.add(reader.nextInt())
  }
  val x = reader.nextInt()

  var result = -1
  list.forEachIndexed { i, v ->
    if (v == x){
      result = i
    }
  }

  if (result != -1){
    println("Número da poltrona do vencedor: $result")
  } else {
    println("Não há vencedor")
  }
}