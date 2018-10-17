package week6.knapsack

//package week5

import scala.util.Random
//import Main.editDistance

object StressTestEditDistance {

  def run(args: Array[String]): Unit = {
    val n = 5
    val m = 5
    runStressTest(n, m)
  }

  def runStressTest(n: Int, m: Int): Unit = {
    val rng = new Random()
    val x = "exponential".toList
    val y = "polynomial".toList
//    val x = rng.alphanumeric.take(n).mkString.toList
//    val y = rng.alphanumeric.take(m).mkString.toList
//    println(x, y)
//    editDistance(x, y)
  }

}
