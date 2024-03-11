package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val months = mapOf(
    1 to "Janeiro",
    2 to "Fevereiro",
    3 to "Março",
    4 to "Abril",
    5 to "Maio",
    6 to "Junho",
    7 to "Julho",
    8 to "Agosto",
    9 to "Setembro",
    10 to "Outubro",
    11 to "Novembro",
    12 to "Dezembro",
  )

  val n = reader.nextInt()
  println(months[n])
}
