package week5

import scala.util.Random
import ChangeMoney.changeMoney

object StressTestChangeMoney {

  def main(args: Array[String]): Unit = {
    val n = math.pow(10, 2).toInt
    val m = 1000
    runStressTest(n, m)
  }

  def runStressTest(n: Int, m: Int): Unit = {
    val rng = new Random()
    for (i <- 1 to m) {
      var x = rng.nextInt(n)
      x = if (x == 0) 1 else x
      val resultNaive = changeMoneyBruteForce(x)
      val result = changeMoney(x)
      println(s"x: $x")
      println(s"naive: $resultNaive")
      println(s"test: $result")
      println()
//      if (resultNaive != result) {
//        println("Failure")
//        return
//      }
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
