package problems.pro

import java.util.Scanner
// Testing another comment
fun main(){
  val reader = Scanner(System.`in`)
  var matrix = mutableListOf<MutableList<Int>>()

  while (reader.hasNextLine()){
    val inp = reader.nextLine()
    if (inp.isBlank()){
      break
    }

    val ints = inp.split(" ").map { it.toInt() }.toMutableList()
    matrix.add(ints)
  }

  var size = matrix[0].size

  while(size > 1){
    var r = 0
    var c = 0

    val diagonalIndices = (0 until size).toList()
    val antiDiagonalIndices = (0 until size).map { size - 1 - it }

    for (i in diagonalIndices){
      r += matrix[i][i]
      c += matrix[i][antiDiagonalIndices[i]]
    }

    val rowRemove = r % size
    val colRemove = c % size

    // Delete
    matrix = matrix.filterIndexed { index, _ -> index != rowRemove }.toMutableList()
    matrix = matrix.map { row -> row.filterIndexed { index, _ -> index != colRemove }.toMutableList() }.toMutableList()

    size--
  }

  println(matrix[0][0])

}
