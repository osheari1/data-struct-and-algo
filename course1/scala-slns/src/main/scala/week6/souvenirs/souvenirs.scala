//package week6.souvenirs

import scala.collection.mutable.ArrayBuffer


object souvenirs extends App {

  override def main(args: Array[String]): Unit = {
        val scanner = new java.util.Scanner(System.in)
        val inp1 = scanner.nextLine().toInt
        val inp2 = scanner.nextLine().split(" ") map (_.toInt) toList
    //    val output = if (inp1 % 3 == 0) 1 else 0
    //    println(output)

//    val inp2= List(1, 1, 1)
//    val inp2 = List(17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59)
//    val inp2 = List(3, 3, 3, 3)
//    val inp2= List(1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25)
//    val inp2= List(1, 2, 3, 4, 5, 5)
    val output = souvenir(inp2)
    println(output)

//    val inp3= List(1, 2, 3, 4, 5)
//    val output2 = souvenir(inp3)
//    println(output2)

//    val outputTest = souvenir(inp2)
//    println(outputTest)


    //    val W = inp1(0)
    //    val n = inp1(1)
    //    val ws = scanner.nextLine().split(" ") map (_.toInt) toList

    //    val W = 10
    //    val ws = List(1, 4, 8)

    //    println(s"W: $W, ws: $ws")
    //    val result = knapsack(W, ws)
    //    println(result(result.length-1)(result(0).length-1))
    //    printMatrix(result)
    //    printOut(result, ws)

  }

  def souvenir(inp: List[Int]): Int = {
    val A = 0 :: inp
    if (A.sum % 3 != 0) {
      return 0
    }
    val sum = A.sum / 3

    val M = ArrayBuffer.fill(sum+1, A.length)(0)
    // Initialize top row
    M(0) = M(0).map(_ => 1)
//    for (m <- M) {
//      println(m)
//    }
//    println()


    for {
      i <- 1 until M.length
      j <- 1 until M(0).length
    } {
      M(i)(j) = M(i)(j - 1)
//      println(s"i: $i, j: $j")
      if (i >= A(j)) {
        M(i)(j) = if (M(i)(j) == 1 || M(i - A(j))(j-1) == 1) 1 else 0
      }
    }

//    println(ArrayBuffer(A: _*))
//    for {
//      (m, i) <- M.zipWithIndex
//    } {
//      print(s"$i ")
//      println(m)
//    }

    M.last.last
  }


  def findSum(n: Int, A: List[Int]): Int = {
    for {
      i <- A.indices
    } {
      val c = List.fill(i)(A.slice(0, i))
      val prod = cartesianProduct(c: _*)

      for (p <- prod) {
        if (p.sum == n)
          return 1
      }
    }
    0
  }


  def allCombinations(n: Int, A: List[Int]): Int = {
    val c = List.fill(n)(List(0, 1, 2))
    val prod = cartesianProduct(c: _*)

    for (p <- prod) {
      val sums = ArrayBuffer.fill(3)(0)
      for (i <- 0 until 3) {
        sums(i) = A.indices filter (j => p(j) == i) map (ix => A(ix)) sum
      }

      if (sums(0) == sums(1) && sums(1) == sums(2)) {
        return 1
      }
    }
    0
  }

  def souvenirNaive(A: List[Int]): Int = {

    if (A.sum % 3 != 0) {
      return 0
    }

    val c = List.fill(A.length)(List(0, 1, 2))
    val prod = cartesianProduct(c: _*)
    for (p <- prod) {

      val sums = ArrayBuffer.fill(3)(0)

      for (i <- 0 until 3) {
        sums(i) = A.indices filter (j => p(j) == i) map (ix => A(ix)) sum
      }

      if (sums(0) == sums(1) && sums(1) == sums(2)) {
        return 1
      }
    }
    0
  }


  def cartesianProduct[T](lst: List[T]*): List[List[T]] = {

    /**
      * Prepend single element to all lists of list
      *
      * @param e  single element
      * @param ll list of list
      * @param a  accumulator for tail recursive implementation
      * @return list of lists with prepended element e
      */
    def pel(e: T,
            ll: List[List[T]],
            a: List[List[T]] = Nil): List[List[T]] =
      ll match {
        case Nil => a.reverse
        case x :: xs => pel(e, xs, (e :: x) :: a)
      }

    lst.toList match {
      case Nil => Nil
      case x :: Nil => List(x)
      case x :: _ =>
        x match {
          case Nil => Nil
          case _ =>
            lst.par.foldRight(List(x))((l, a) =>
              l.flatMap(pel(_, a))
            ).map(_.dropRight(x.size))
        }
    }
  }
}
