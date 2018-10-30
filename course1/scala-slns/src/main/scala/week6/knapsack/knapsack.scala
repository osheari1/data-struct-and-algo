//package week6.knapsack

import scala.collection.mutable.ArrayBuffer

object knapsack extends App {

  override def main(args: Array[String]): Unit = {
    val scanner = new java.util.Scanner(System.in)
    val inp1 = scanner.nextLine().split(" ") map (_.toInt)
    val W = inp1(0)
    val n = inp1(1)
    val ws = scanner.nextLine().split(" ") map (_.toInt) toList

//    val W = 10
//    val ws = List(1, 4, 8)

//    println(s"W: $W, ws: $ws")
    val result = knapsack(W, ws)
    println(result(result.length-1)(result(0).length-1))
//    printMatrix(result)
//    printOut(result, ws)

    //    val result = editDistance(word1.toList, word2.toList)
    //    System.out.print(result)
  }


  def knapsack(W: Int, inpWs: List[Int]): ArrayBuffer[ArrayBuffer[Int]] = {
    val matrix = ArrayBuffer.fill(inpWs.length + 1, W + 1)(0)
    val ws = -1 :: inpWs
    for {
      i <- 1 to inpWs.length
      w <- 1 to W
    } {
      //      println(s"w: $w, i: $i")
      matrix(i)(w) = matrix(i - 1)(w)
      if (ws(i) <= w) {
        var value = matrix(i - 1)(w - ws(i)) + ws(i)
        if (value > matrix(i)(w)) {
          matrix(i)(w) = value
        }
      }
    }
    matrix
  }


  def printOut(matrix: ArrayBuffer[ArrayBuffer[Int]], wInp: List[Int]): Unit = {
    val ws = -1 :: wInp
    val wsUsed = ArrayBuffer.fill(ws.length)(0)

    def go(i: Int, w: Int): (Int, Int) = {
      if (i <= 0 && w <= 0){
        return (0,0)
      }

      println(s"i: $i, w: $w, ws(i): ${ws(i)}")
      val current = matrix(i)(w)
      val opt1 = matrix(i-1)(w)
      val opt2 = if (ws(i) <= w) matrix(i-1)(w - ws(i)) + ws(i) else 0
      println(s"opt1: $opt1")
      println(s"opt2: $opt2")
      println(s"current: $current")

      if (opt2 == current) {
        wsUsed(i) = 1
//        println(ws(i))
        println(wsUsed)
        go(i-1, w - ws(i))
      } else if (opt1 == current) {
        wsUsed(i) = 0
//        println(ws(i))
        println(wsUsed)
        go(i-1, w)
      } else {
        (0, 0)
      }
    }

    go(matrix.length-1, matrix(0).length - 1)
    println(s"wsUsed: $wsUsed")
  }

  def printMatrix(matrix: ArrayBuffer[ArrayBuffer[Int]]): Unit = {
    for {
      l <- matrix
    } {
      println(l)
    }
  }
}
