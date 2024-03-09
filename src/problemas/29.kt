package problemas

import java.util.Scanner

/** SOMANDO
 * Dada uma lista de N inteiros, encontre a soma de todos eles.
 *
 *
 * Entrada
 * A entrada é composta de um único caso de teste. A primeira linha contém um inteiro positivo N.
 * As N linhas seguintes contêm cada uma um inteiro X, representando os N números a serem somados.
 *
 *
 * Saída
 * Seu programa deve produzir uma única linha na saída, contendo a soma de todos os N inteiros.
 *
 *
 * **/

fun main() {
    val reader = Scanner(System.`in`)
    val n = reader.nextInt()
    val list = mutableListOf<Int>()

    for (i in 0 until n){
        list.add(reader.nextInt())
    }

    println(list.sum())
}
