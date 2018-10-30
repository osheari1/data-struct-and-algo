package week5.lcs3

import scala.util.Random
//import Main.editDistance

object StressTestLCS3 {

  def main(args: Array[String]): Unit = {
    val n = 5
    val m = 5
    val o = 5
    runStressTest(n, m, o)
  }

  def runStressTest(n: Int, m: Int, o: Int): Unit = {
    val rng = new Random()
//    val x = "exponential".toList
//    val y = "polynomial".toList
//    val z = "polyglot".toList

//    val x = (0 to n) map (_ => rng.nextInt(10)) toList
//    val y = (0 to m) map (_ => rng.nextInt(10)) toList
//    val z = ((0 to o) map (_ => rng.nextInt(10))).toList
//    val x = -1::List(1, 2, 3)
//    val y = -1::List(2, 3, 1)
    val x = -1::List(1, 2, 3)
    val y = -1::List(2, 1, 3)
    val z = -1::List(1, 3, 5)
    println(x, "\n", y, "\n", z)
//    println(LCS3.lcs3(x, y, z))
    println(LCS3.lcs3(x, y, z))
  }

}
