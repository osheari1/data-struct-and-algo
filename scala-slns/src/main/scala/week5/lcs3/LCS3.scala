//package week5.lcs3

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
    val result = lcs3(-1::word1, -1::word2, -1::word3)
//    val result = lcs2(-1::word1, -1::word2)
    System.out.print(result)
  }

  def lcs2(w1: List[Int], w2: List[Int]): Int = {
    val m = ArrayBuffer.fill(
      w1.length, w2.length
    )(0)

    val b = ArrayBuffer.fill(
      w1.length, w2.length
    )(0)

    val cost = (i: Int, j: Int) => {

//      println(s"w1: ${w1(i)}")
//      println(s"w2: ${w2(j)}")
      var maxes = List(if (w1(i) == w2(j))
        m(i-1)(j-1) + 1
      else
        0
      )

      for {
        a <- 0 to 1
        b <- 0 to 1
      } {
//        println(s"m(${i-a})(${j-b}): ${m(i-a)(j-b)}")
        val test =  if (a == 1 && b == 1) {
          0
        } else if (a == 0 && b == 0) {
          0
        } else {
          m(i-a)(j-b)
        }
        maxes = test :: maxes
      }
//      println(s"maxes: $maxes")
      maxes.max
    }

    for {
      i <- 1 until w1.length
      j <- 1 until w2.length
    } {
      m(i)(j) = cost(i, j)
//      print(s"location: $i, $j")
//      println(s"\tscore: ${m(i)(j)}")
      //      print(m(i)(j)(k))
    }
    m(w1.length-1)(w2.length-1)
  }



  def lcs3(w1: List[Int], w2: List[Int], w3: List[Int]): Int = {
    val m = ArrayBuffer.fill(
      w1.length, w2.length, w3.length
    )(0)

    val b = ArrayBuffer.fill(
      w1.length, w2.length, w3.length
    )(0)

    val cost = (i: Int, j: Int, k: Int) => {

//      println(s"w1: ${w1(i)}")
//      println(s"w2: ${w2(j)}")
//      println(s"w3: ${w3(k)}")
      val max = if (w1(i) == w2(j) && w2(j) == w3(k) && w1(i) == w3(k))
        m(i-1)(j-1)(k-1) + 1
      else {
        List(m(i-1)(j)(k), m(i)(j-1)(k), m(i)(j)(k-1)).max
      }
//
//      for {
//        a <- 0 to 1
//        b <- 0 to 1
//        c <- 0 to 1
//      } {
//        println(s"m(${i-a})(${j-b})(${k-c}): ${m(i-a)(j-b)(k-c)}")
//        val test =  if (a == 1 && b == 1 && c ==1) {
//          0
//        } else {
//          m(i-a)(j-b)(k-c)
//        }
//        maxes = test :: maxes
//      }
//      println(s"max: $max")
      max
    }

    for {
      i <- 1 until w1.length
      j <- 1 until w2.length
      k <- 1 until w3.length
    } {
      m(i)(j)(k) = cost(i, j, k)
      for {
        a <- 0 to 1
        b <- 0 to 1
        c <- 0 to 1
      } {
//        println(s"m(${i - a})(${j - b})(${k - c}): ${m(i - a)(j - b)(k - c)}")
      }
//      print(s"location: $i, $j, $k")
//      println(s"\tscore: ${m(i)(j)(k)}")
//      print(m(i)(j)(k))
    }
    m(w1.length-1)(w2.length-1)(w3.length-1)
  }

//  def printLCM3(b: List[List[List[Int]]], w, i, j): Unit = {
//
//
//  }

}
