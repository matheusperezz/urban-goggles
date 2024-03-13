package problems.starter

import java.lang.String.format
import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val n = reader.nextFloat()
  val fee: Float = when {
    n <= 400F -> 15.0F
    n <= 800.00F -> 12.0F
    n <= 1200.00F -> 10.0F
    n <= 2000.00F -> 7.0F
    else -> 4.0F
  }

  val curr = n*(fee/100) + n

  println("""
    Novo salario: ${format("%.2f", curr)}
    Reajuste ganho: ${format("%.2f", curr-n)}
    Em percentual: ${format("%.0f", fee)} %
  """.trimIndent())
}
