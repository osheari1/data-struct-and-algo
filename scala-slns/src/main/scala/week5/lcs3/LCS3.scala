package week5.lcs3

import scala.collection.mutable.ArrayBuffer

object LCS3 extends App {

  override def main(args: Array[String]): Unit = {
    val scanner = new java.util.Scanner(System.in)
    val x = scanner.nextLine()
    val word1 = scanner.nextLine().split(" ").map(_.toInt).toList
    val y = scanner.nextLine()
    val word2 = scanner.nextLine().split(" ").map(_.toInt).toList
    val z = scanner.nextLine()
    val word3 = scanner.nextLine().split(" ").map(_.toInt).toList
    val result = lcs3(word1, word2, word3)
//    print(word1)
    System.out.print(result)
  }

//  val cost = { i: Int => {
//    j: Int => {
//      k: Int => {
//        m: ArrayBuffer[ArrayBuffer[ArrayBuffer[Int]]] => {
//          var max = Int.MaxValue
//          for {
//            a <- 0 to 1
//            b <- 0 to 1
//            c <- 0 to 1
//          } {
//            if (m(i-a)(j-b)(k-c) > max)
//              max = m(i-a)(j-b)(k-c)
//          }
//          max
//        }
//      }
//    }
//  }


//    def cost(i: Int, j: Int, k: Int, m: ArrayBuffer[ArrayBuffer[ArrayBuffer[Int]]]): Int = {
//      var max = 0
//      for {
//        a <- 0 to 1
//        b <- 0 to 1
//        c <- 0 to 1
//      } {
//        if ()
//        if (m(i-a)(j-b)(k-c) > max)
//          max = m(i-a)(j-b)(k-c)
//      }
//      max
//    }

  def lcs3(w1: List[Int], w2: List[Int], w3: List[Int]): Int = {
    val m = ArrayBuffer.fill(
      w1.length+1, w2.length+1, w3.length+1
    )(0)
    val b = ArrayBuffer.fill(
      w1.length+1, w2.length+1, w3.length+1
    )(0)
    val cost = (i: Int, j: Int, k: Int, m: ArrayBuffer[ArrayBuffer[ArrayBuffer[Int]]]) => {
      var max = 0
      for {
        a <- 0 to 1
        b <- 0 to 1
        c <- 0 to 1
      } {
        val test =  if (a == 1 && b == 1 && c ==1) {
          if (w1(i-1) == w2(j-1) && w2(j-1) == w3(k-1) && w1(i-1) == w3(k-1))
            m(i-a)(j-b)(k-c) + 1
          else
            m(i-a)(j-b)(k-c)
        } else {
          m(i-a)(j-b)(k-c)
        }

        if (test > max)
          max = test
      }
      max
    }

    for {
      i <- 1 to w1.length
      j <- 1 to w2.length
      k <- 1 to w3.length
    } {
      m(i)(j)(k) = cost(i, j, k, m)
      print(m(i)(j)(k))
    }
    m(w1.length)(w2.length)(w3.length)
  }

//  def printLCM3(b: List[List[List[Int]]], w, i, j): Unit = {
//
//
//  }

}
