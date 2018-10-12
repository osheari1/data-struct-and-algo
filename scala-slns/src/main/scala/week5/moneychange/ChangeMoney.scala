package week5

//import scala.annotation.tailrec

object ChangeMoney extends App {

  override def main(args: Array[String]): Unit = {
    val scanner = new java.util.Scanner(System.in)
    val money = scanner.nextLine().toInt
    val result = changeMoney(money)
    System.out.print(result)
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

  def changeMoney(M: Int): Int = {
    val cs = List(1, 3, 4)
    val minC = List.fill(M+1)(Int.MaxValue).updated(0, 0)
    val m = M
//    println(s"M: $M")
//    println(s"m: $m")

    def go(i: Int, minC: List[Int]): List[Int] = {
      var minCurrent = minC(i)
//      println(s"i: $i")
//      println(s"m-i: ${m - i}")
//      println(s"minCurrent: ${minC(i)}")

      for (c <- cs) {
//        println(s"c: $c")
        if (c <= i) {
          if (minC(i-c) + 1 < minCurrent)
            minCurrent = minC(i - c) + 1
        }
      }
//      println(s"newMin: $minCurrent")
      if (i == m) {
        return minC.updated(m, minCurrent)
      }
      go(i+1, minC.updated(i, minCurrent))
    }
    val newMinc = go(1, minC)
//    println(newMinc)
    newMinc(m)
  }


}
