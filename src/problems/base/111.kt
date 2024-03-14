package problems.base

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val matrix = mutableListOf<MutableList<Int>>()
  val rows = reader.nextInt()
  val columns = reader.nextInt()

  for (i in 0 until rows){
    val row = mutableListOf<Int>()
    for (j in 0 until columns){
      row.add(reader.nextInt())
    }
    matrix.add(row)
  }

  var total = 0
  for (i in 0 until rows){
    if (i % 2 == 0){
      for (j in 0 until columns){
        total += matrix[i][j]
        if (total < 0) total = 0
      }
    } else {
      for (j in columns - 1 downTo 0){
        total += matrix[i][j]
        if (total < 0) total = 0
      }
    }
  }

  println(total)
}