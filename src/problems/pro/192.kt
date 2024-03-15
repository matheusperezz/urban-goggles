package problems.pro

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val matrix = mutableListOf<MutableList<String>>()

  for (i in 0 until 10){
    val row = reader.nextLine().split(" ").toMutableList()
    matrix.add(row)
  }

  var hasOrcMage = false
  for (i in 0 until 10){
    for (j in 0 until 5){
      if (matrix[i][j] == "m"){
        hasOrcMage = true
      }
    }
  }

  var hasHumanMage = false
  for (i in 0 until 10){
    for (j in 5 until 10){
      if (matrix[i][j] == "m"){
        hasHumanMage = true
      }
    }
  }

  for (i in 0 until 10){
    for (j in 0 until 5){
      if (matrix[i][j] == "m"){
        hasOrcMage = true
      }
    }
  }

  val orcPower = orcCalc(matrix, hasOrcMage)
  val humanPower = humanCalc(matrix, hasHumanMage)
  println("orcPower = $orcPower humanPower = $humanPower")
}

private fun orcCalc(matrix: MutableList<MutableList<String>>, hasMage: Boolean): Int{
  var power = 0
  val type = "o"
  for (i in 0 until 10){
    for (j in 0 until 5){
      // UP
      var curr = 0
      if (matrix[i][j] == type || matrix[i][j] == "m"){
        if (i != 0 && matrix[i][j] == type){
          curr++
        }
        // RIGHT
        if (j != 4 && matrix[i][j] == type){
          curr++
        }
        // DOWN
        if (i != 9 && matrix[i][j] == type){
          curr++
        }
        // LEFT
        if (j != 0 && matrix[i][j] == type){
          curr++
        }
        if (curr >= 2 && hasMage){
          power += 3
        } else {
          power++
        }
      }
    }
  }
  return power
}

private fun humanCalc(matrix: MutableList<MutableList<String>>, hasMage: Boolean): Int{
  var power = 0
  val type = "h"
  for (i in 0 until 10){
    for (j in 5 until 10){
      var curr = 0
      // UP
      if (matrix[i][j] == type || matrix[i][j] == "m"){
        if (i != 0 && matrix[i][j] == type){
          curr++
        }
        // RIGHT
        if (j != 9 && matrix[i][j] == type){
          curr++
        }
        // DOWN
        if (i != 9 && matrix[i][j] == type){
          curr++
        }
        // LEFT
        if (j != 5 && matrix[i][j] == type){
          curr++
        }
        if (curr == 4 && hasMage){
          power += 5
        } else {
          power++
        }
      }
    }
  }
  return power
}