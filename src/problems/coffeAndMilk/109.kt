package problems.coffeAndMilk

import java.util.*

fun main() {
  val reader = Scanner(System.`in`)
  val lux = reader.nextInt()
  val ekko = reader.nextInt()

  if (lux > ekko){
    println(lux)
    println("Lux")
  } else if (ekko > lux){
    println(ekko)
    println("Ekko")
  } else {
    println(lux)
    println("Os dois tem a mesma quantidade de poder")
  }
}