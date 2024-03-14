package problems.base

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val matrix = mutableListOf<MutableList<Int>>()

  for (i in 0 until 7){
    val row = mutableListOf<Int>()
    for (j in 0 until 7){
      row.add(reader.nextInt())
    }
    matrix.add(row)
  }

  var total = 0
  for (j in 0 until 7){
    for (i in 0..j){
      if (matrix[i][j] == 1){
        total++
      }
    }
  }

  println(total)
}