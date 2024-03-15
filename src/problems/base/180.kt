package problems.base

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val matrix = mutableListOf<MutableList<Int>>()

  for (i in 0 until 8) {
    val row = mutableListOf<Int>()
    for (j in 0 until 8) {
      row.add(reader.nextInt())
    }
    matrix.add(row)
  }

  val x = reader.nextInt()
  val y = reader.nextInt()

  // Code
  var total = 0

  // left
  for (j in x-1 downTo 0 ){
    if (matrix[x][j] == 1){
      break
    } else if (matrix[x][j] == 2){
      total++
      break
    }
  }

  // right
  for (j in x+1 until 8 ){
    if (matrix[x][j] == 1){
      break
    } else if (matrix[x][j] == 2){
      total++
      break
    }
  }

  // up
  for (i in y-1 downTo 0){
    if (matrix[i][y] == 1){
      break
    } else if (matrix[i][y] == 2){
      total++
      break
    }
  }

  // down
  for (i in y+1 until 8){
    if (matrix[i][y] == 1){
      break
    } else if (matrix[i][y] == 2){
      total++
      break
    }
  }

  println(total)
}