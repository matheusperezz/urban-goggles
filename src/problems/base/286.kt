package problems.base

import java.util.*

fun main() {
  val reader = Scanner(System.`in`)
  val hp = reader.nextInt()
  var atk = reader.nextInt()

  // PA Sum
  val pa = ((1 + atk) * atk) / 2
  if (pa < hp){
    println("F")
    return
  }

  var count = 0
  var total = 0
  while (total < hp){
    total += atk
    count++
    atk--
  }

  println(count)
}

