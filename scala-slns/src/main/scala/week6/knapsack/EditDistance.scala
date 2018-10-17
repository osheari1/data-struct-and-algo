package week6.knapsack

import scala.collection.mutable.ArrayBuffer

object EditDistance extends App {

  override def main(args: Array[String]): Unit = {
    val scanner = new java.util.Scanner(System.in)
    val word1 = scanner.nextLine()
    val word2 = scanner.nextLine()
    val result = editDistance(word1.toList, word2.toList)
    System.out.print(result)
  }

  def editDistance(word1: List[Char], word2: List[Char]): Int = {
    val eMatrix = ArrayBuffer.fill(word1.length+1, word2.length+1)(0)

    // fill in 0 column of eMatrix
    for (ix <- 0 to word1.length.max(word2.length)) {
      if (ix <= word1.length)
        eMatrix(ix).update(0, ix)
      if (ix <= word2.length)
        eMatrix(0).update(ix, ix)
    }

    for (i <- 1 to word1.length) {
      for (j <- 1 to word2.length) {
        eMatrix(i).update(
          j,
          List(
            eMatrix(i-1)(j) + 1,
            eMatrix(i)(j-1) + 1,
            if (word1(i-1) == word2(j-1)) eMatrix(i-1)(j-1) else eMatrix(i-1)(j-1)+1
        ).min)
      }
    }

//    print(eMatrix.mkString("\n"))
//    println()
    eMatrix(word1.length)(word2.length)
  }


}
