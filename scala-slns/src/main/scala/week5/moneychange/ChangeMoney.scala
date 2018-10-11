//package week5

object ChangeMoney extends App {

  override def main(args: Array[String]): Unit = {
    val scanner = new java.util.Scanner(System.in)
    val money = scanner.nextLine().toInt
    val result = changeMoneyBruteForce(money)
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

//  def changeMoney(m: Int): Int = {
//    0
//  }


}
