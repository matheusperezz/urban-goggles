package problems.base

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val n = reader.nextInt()
  println(fee(n))
}

fun fee(n: Int): Int{
  var totalFee = 7
  if (n > 10) {
    totalFee += minOf(n, 30) - 10
    if (n > 30) {
      totalFee += 2 * (minOf(n, 100) - 30)
      if (n > 100) {
        totalFee += 5 * (n - 100)
      }
    }
  }
  return totalFee
}