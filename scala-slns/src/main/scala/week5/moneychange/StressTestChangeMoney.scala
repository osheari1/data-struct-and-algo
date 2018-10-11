package week5

import scala.util.Random
//import Main.editDistance

object StressTestChangeMoney {

  def main(args: Array[String]): Unit = {
    val n = 10
    val m = 10
    runStressTest(n, m)
  }

  def runStressTest(n: Int, m: Int): Unit = {
    val rng = new Random()
    for (i <- 0 to m) {
      val x = rng.nextInt(n)
      val result = changeMoneyBruteForce(x)
//      println(s"x: $x, result: $result")
      println("result")
    }
  }

  def changeMoneyBruteForce(m: Int): Int = {
    val ds = List(1.0, 3.0, 4.0)

    var minNC = Double.PositiveInfinity
    for {
      i_1 <- 0 to math.floor(m / ds.head).toInt
      i_3 <- 0 to math.floor(m / ds(1)).toInt
      i_4 <- 0 to math.floor(m / ds(2)).toInt
    } {
      val value = ((ds zip List(i_1, i_3, i_4)) map Function.tupled(_ * _)).sum

      if (value == m) {
        val numCoins = List(i_1, i_3, i_4).sum
        if (numCoins < minNC) {
          minNC = numCoins.toDouble
        }
      }
    }
    minNC.toInt
  }
}
