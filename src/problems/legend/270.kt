package problems.legend

// TODO: Teste 5 falhando
import java.util.Scanner
import kotlin.math.pow
import kotlin.math.round

fun main() {
  val reader = Scanner(System.`in`)
  val keyword = mapOf(
    "carro" to "%",
    "acidente" to "$",
    "senhor" to "&",
    "do" to "#"
  )
  val s = mutableListOf<String>()
  while (reader.hasNextLine()){
    val line = reader.nextLine()
    if (line.isBlank()){
      break
    }
    s.add(line)
  }


  val text = s.joinToString(" ")
  val initialSize = text.length.toDouble()

  val words = text.split(Regex("\\b"))
  val replacedWords = words.map { word ->
    val trimmedWord = word.trimEnd { it in ".," }
    keyword.entries.find { "\\b${it.key}\\b".toRegex().containsMatchIn(trimmedWord) }?.let {
      it.value + word.drop(it.key.length)
    } ?: word
  }
  val replacedText = replacedWords.joinToString("")
  val finalSize = replacedText.length.toDouble()

  val compressionRate = roundUp(finalSize / initialSize, 2)

  println(replacedText)
  println("Taxa de compressao:%.2f".format(compressionRate) + "%")
}

fun roundUp(number: Double, decimal: Int): Double {
  val factor = 10.0.pow(decimal)
  return round(number * factor + 0.5) / factor
}
