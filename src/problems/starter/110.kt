package problems.starter

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

  val p = reader.nextInt()

  var count = 0
  for (i in 0 until rows){
    for (j in 0 until columns){
      if (matrix[i][j] == p){
        count++
      }
    }
  }

  println("Ash pegou $count pokemon")
}