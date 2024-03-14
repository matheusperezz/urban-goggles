package problems.base

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val list = mutableListOf<Int>()
  val matrix = mutableListOf<MutableList<Int>>()
  val pairs = mutableSetOf<Pair<Int, Int>>()
  val n = reader.nextInt()
  val m = reader.nextInt()


  for (i in 0 until n) {
    val row = mutableListOf<Int>()
    for (j in 0 until n) {
      row.add(reader.nextInt())
    }
    matrix.add(row)
  }

  for (k in 0 until m*2){
    list.add(reader.nextInt())
  }

  for (l in 0 until m*2 step 2){
    val x = list[l]
    val y = list[l+1]
    hasEnemy(matrix, x, y, pairs)
  }

  println(pairs.count())

}

private fun hasEnemy(matrix: MutableList<MutableList<Int>>, x: Int, y: Int, pairs: MutableSet<Pair<Int, Int>>){
  for (j in x downTo 0) {
    if (matrix[j][y] == 1){
      matrix[j][y] = 0
      pairs.add(Pair(j,y))
      break
    }
  }
}