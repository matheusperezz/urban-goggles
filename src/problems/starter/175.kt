package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val matrix = mutableListOf<MutableList<Int>>()
  val n = reader.nextInt()
  val m = reader.nextInt()


  for (i in 0 until n) {
    val row = mutableListOf<Int>()
    for (j in 0 until m) {
      row.add(reader.nextInt())
    }
    matrix.add(row)
  }

  reader.nextLine()

  val (pos, qnt) = reader.nextLine().split(" ")
  var total = 0
  val qntInt = qnt.toInt()-1
  if (pos == "L"){
    total = matrix[qntInt].sum()
  } else {
    for (i in 0 until n){
      for (j in 0 until m){
        if (j == qntInt){
          total += matrix[i][j]
        }
      }
    }
  }
  println(total)
}