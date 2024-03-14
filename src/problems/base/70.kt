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
  var colSum = MutableList(columns) { 0 }

  for (i in 0 until rows){
    var rowSum = 0
    for (j in 0 until columns){
      val value = matrix[i][j]
      rowSum += value
      colSum[j] += value
    }
    total = maxOf(total ,rowSum)
  }

  for (c in colSum){
    total = maxOf(total, c)
  }

  println(total)
}