package problems.starter

import java.util.Scanner

fun main() {
  val reader = Scanner(System.`in`)
  val e1 = reader.nextInt()
  val e2 = reader.nextInt()
  val e3 = reader.nextInt()

  val p1 = reader.nextInt()
  val p2 = reader.nextInt()
  val p3 = reader.nextInt()

  val eggs = e1 + e2 + e3
  val toxics = (p1 + p2 + p3) * 3
  println(eggs - toxics)
}
