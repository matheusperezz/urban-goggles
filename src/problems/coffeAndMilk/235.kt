package problems.coffeAndMilk

import java.util.Scanner

fun main(){
  val reader = Scanner(System.`in`)
  val sc = reader.nextInt()
  val mm = reader.nextInt()
  val ck = reader.nextInt()

  if (sc == 30){
    println("PROXIMO MUNDO")
  } else {
    println("${30-sc} ${6-mm} ${3-ck}")
  }
}