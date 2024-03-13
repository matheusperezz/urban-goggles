package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val rk = reader.nextInt()
  val rj = reader.nextInt()
  val rh = reader.nextInt()
  val ck = reader.nextInt()
  val cj = reader.nextInt()
  val ch = reader.nextInt()

  println("${rk+ck} ${rj+cj} ${rh+ch}")
}