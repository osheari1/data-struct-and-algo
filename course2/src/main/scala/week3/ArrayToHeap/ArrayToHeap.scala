//package week3.ArrayToHeap

import java.util.Scanner

import scala.annotation.tailrec
import scala.collection.mutable.ArrayBuffer
import scala.util.Random

/** Constraints
  * 1 <= n <= 100000
  * 0 <= i, j <= n-1
  * 0 <= a0, a1, a2...an-1 <= 10^9 all ai are distinct
  *
  * output:
  * 0 <= m <= 4n
  * Must satisfy
  * if 2i+1 <= n-1 then a_i < a_2i+1
  * if 2i+2 <= n-1 then a_i < a_2i+2
  *
  */
//noinspection ScalaDocParserErrorInspection,ScalaDocUnclosedTagWithoutParser


class Heap(val prod: Boolean = false) {
  var swaps = Array[(Int, Int)]()
  var swapIx = 0
  //  var swaps = List[(Int, Int)]()
//  var dataOrig = Array[Int]()
//  var dataSorted = Array[Int]()
  var data = Array[Int]()
  var maxSize = this.data.length
  var size = 0

  def time[R](block: => R): R = {
    val t0 = System.currentTimeMillis()
    val result = block // call-by-name
    val t1 = System.currentTimeMillis()
    val t = t1 - t0
    println("Elapsed time: " + (t1 - t0) + "ms")
    result
  }

  private val rng = new Random(1)
//  var dataNaive = Array[Int]()

  private def swap(i: Int, j: Int): Unit = {
    val tmp = this.data(i)
    this.data(i) = this.data(j)
    this.data(j) = tmp
    //    this.swaps = (i, j) :: this.swaps
    this.swaps(this.swapIx) = (i, j)
    this.swapIx += 1
//    this.swaps.append((i, j))
  }

  def buildHeap(): Unit = {
    //    time {
    for (i <- (math.floor(this.size) / 2).toInt to 0 by -1) {
      this.siftDown(i)
    }
    //      this.swaps = this.swaps.reverse
    //    }
  }

  def parent(i: Int): Int = math.floor((i - 1) / 2).toInt

  def leftChild(i: Int): Int = 2 * i + 1

  def rightChild(i: Int): Int = 2 * i + 2

  @tailrec
  final def siftUp(i: Int): Unit =
    if (i > 0 & this.data(parent(i)) > i) {
      this.swap(i, parent(i))
      siftUp(parent(i))
    }

  @tailrec
  final def siftDown(i: Int): Unit = {
    var minIx = i
    val l = leftChild(i)
    val r = rightChild(i)
    if (l <= this.size - 1 && this.data(l) < this.data(minIx)) {
      minIx = l
    }
    if (r <= this.size - 1 && this.data(r) < this.data(minIx)) {
      minIx = r
    }
    if (i != minIx) {
      this.swap(i, minIx)
      siftDown(minIx)
    }
  }

  def extractMax(): Int = {
    val result = this.data(0)
    this.data(0) = this.data(this.size - 1)
    this.size = this.size - 1
    siftDown(0)
    result
  }

  def sort() = {
    while (this.size > 0) {
      this.swap(0, this.size - 1)
      this.size = this.size - 1
      this.siftDown(0)
    }
    this.data = this.data.reverse
  }

  def readData(): Unit = {
    val scanner = new Scanner(System.in)
    val n = scanner.nextLine().toInt
    val arr = scanner.nextLine().split(" ").map(_.toInt)
    assert(n == arr.length)
    this.data = arr
    this.reset()
  }


  def readRandom(n: Int): Unit = {
    this.data = this.rng.shuffle((0 until n).toList).toArray
    this.reset()
  }

  def reset(): Unit = {
    if (!this.prod) {
//      this.dataOrig = this.data.clone()
      //      this.swaps = List[(Int, Int)]()
//      this.swaps.clear()
    }
    this.swaps = Array.ofDim[(Int, Int)](this.data.length)
    this.maxSize = this.data.length
    this.size = this.data.length
  }

  def buildHeapNaive(): Unit = {
    for {
      i <- this.data.indices
      j <- i + 1 until this.data.length
    } {
      if (this.data(i) > this.data(j)) {
        this.swap(i, j)
      }
    }
    this.swaps = this.swaps.reverse
  }

  def writeResponse(): Unit = {
//    println(this.swaps.length)
    println(this.swapIx)
    //    println(this.swaps)
    for (i <- 0 until swapIx) {
      val s = this.swaps(i)
      println(s"${s._1} ${s._2}")
    }
    println()
  }

  def solve(read: Boolean = true): Unit = {
    if (read)
      this.readData()
    else {
//      this.data = this.dataOrig.clone()
      this.reset()
    }
    this.buildHeap()
  }

  def solveNaive(read: Boolean = true): Unit = {
    if (read)
      this.readData()
    else {
//      this.data = this.dataOrig.clone()
      this.reset()
    }
    this.buildHeapNaive()
//    this./**/dataNaive = this.data.clone()
  }

  def printData(): Unit = {
    // first sort heap then print

    print("\nOrig: ")
//    this.dataOrig.foreach(a => print(s"$a "))

    print("\nHeap: ")
    this.data.foreach(a => print(s"$a "))

    print("\nSorted: ")
    this.sort()
    this.data.foreach(a => print(s"$a "))
    print("\n")
  }

  def printDataNaive(): Unit = {

    print("Naive Sorted: ")
//    this.dataNaive.foreach(a => print(s"$a "));
  }

}


object ArrayToHeap extends App {
  override def main(args: Array[String]): Unit = {
    run()
    //    runRandom()
  }

  def runRandom(): Unit = {
    val m = 100
    val n = 100
    for {_ <- 0 until m} {
      val h = new Heap()
      h.readRandom(n)
      h.buildHeap()
      h.printData()
      val test = h.data

      h.solveNaive(false)
      h.printDataNaive()
      println()
      if (!(test sameElements h.data)) {
        println("FAIL")
        return
      }
    }
  }


  def run(): Unit = {
    val h = new Heap(true)
    h.solve()
    h.writeResponse()
    //    val h = new Heap(true)
    //    h.readRandom(100000)
    //    time {
    //      h.buildHeap()
    //    }
    //    h.writeResponse()
    //    h.printData()

    //    h.solveNaive(read = false)
    //    h.printDataNaive()
    //    println()
    //    h.writeResponse()
    //    h.readData()
    //    h.buildHeapNaive()
    //    h.printData()
    //    h.printDataNaive()
  }

  def time[R](block: => R): R = {
    val t0 = System.currentTimeMillis()
    val result = block // call-by-name
    val t1 = System.currentTimeMillis()
    val t = t1 - t0
    println("Elapsed time: " + (t1 - t0) + "ms")
    result
  }

}


