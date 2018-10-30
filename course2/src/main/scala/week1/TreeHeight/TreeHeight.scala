package week1.TreeHeight

import scala.collection.mutable
import scala.collection.mutable.ListBuffer
import scala.util.Random

object TreeHeight extends App {

  //  override def main(args: Array[String]): Unit = {
  //    val scanner = new Scanner(System.in)
  //    val n = scanner.nextLine().toInt
  //    val inp = scanner.nextLine().split(" ").map(_.toInt)
  //    val (tree, root) = buildTree(n, inp)
  //    val output = treeHeight(tree, root)
  //    println(output)
  //  }

  override def main(args: Array[String]): Unit = {
    //      //      val inps = List(
    //      //        (100, "32 7 51 65 35 72 63 84 60 87 33 24 43 86 9 68 26 64 6 43 32 35 18 82 33 75 94 19 59 12 54 29 75 -1 12 12 58 7 17 60 75 95 64 95 51 76 50 87 53 65 10 33 46 93 64 82 5 80 10 12 12 50 87 59 68 50 42 95 10 9 43 64 33 36 20 95 75 42 75 15 59 50 4 41 43 18 43 83 72 81 1 43 1 60 43 68 93 63 95 63".split(" ").map(_.toInt).toList),
    //      //        (5, List(-1, 0, 4, 0, 3)),
    //      //        (5, List(4, -1, 4, 1, 1)),
    //      //      )
    //
    val m = 100
    val seed = 1
    val rng = new Random(seed)
    val nMax = scala.math.pow(10, 6).toInt
    val inps = Array.fill(m) {
      val n = rng.nextInt(nMax) + 1
      val values = Array.fill(n) {
        rng.nextInt(n)
      }
      (n, values.updated(rng.nextInt(values.length), -1))
    }

    var totalTimeBuild = 0.0
    var totalTimeHeight = 0.0
    inps.foreach { inp =>

      val ((tree, rootIx), t) = buildTreeTime2(inp._1, inp._2.toArray)
      totalTimeBuild += t

      //        tree.foreach { x =>
      //          println(x)
      //        }

      val (output, th) = time {
        treeHeight(tree, rootIx)
      }
      totalTimeHeight += th
      //        val outputNaive = treeHeightNaive(inp._1, inp._2.toList)
      println(s"output: $output")
      println()
      //        println(s"outputNaive: $outputNaive")
    }
    println(s"AvgtimeBuild: ${totalTimeBuild / m}")
    println(s"AvgtimeHeight: ${totalTimeHeight / m}")
  }

  //  type Node = ArrayBuffer[Int]
  type Node = List[Int]

  def treeHeight(tree: Array[Node], root: Int): Int = {
    val q = mutable.Queue[Node]()
    val qH = mutable.Queue[Int]()
    val hs = ListBuffer[Int]()
    q.enqueue(tree(root))
    qH.enqueue(1)
    while (q.nonEmpty) {
      val node = q.dequeue()
      val h = qH.dequeue()
      //      println(node)
      if (node.nonEmpty) {
        for (child <- node) {
          q.enqueue(tree(child))
          qH.enqueue(h + 1)
        }
      } else {
        hs.append(h)
      }
    }
    hs max
  }

  def buildTreeTime(n: Int, parents: Array[Int]) = {
    time {
      var root = 0
      val nodes = Array.fill(n)(List[Int]())
      nodes.indices.foreach { childIx =>
        parents(childIx) match {
          case -1 => root = childIx
          case pIx => nodes(pIx) match {
            case node => nodes(pIx) = childIx :: node
          }
        }
      }
      (nodes, root)
    }
  }

  def buildTreeTime2(n: Int, parents: Array[Int]) = {
    time {
      var root = 0
//      val nodes = Array.fill(n)(List[Int]())
      val nodes = Array.fill(n)(List[Int]())
      nodes.indices.foreach { childIx =>
        parents(childIx) match {
          case -1 => root = childIx
          case pIx => nodes(pIx) match {
            case node => nodes(pIx) = childIx :: node
          }
        }
      }
      (nodes, root)
    }
  }

  def buildTree(n: Int, parents: Array[Int]) = {
    var root = 0
    val nodes = Array.fill(n)(List[Int]())
    nodes.indices.foreach { childIx =>
      parents(childIx) match {
        case -1 => root = childIx
        case pIx => nodes(pIx) match {
          case node => nodes(pIx) = childIx :: node
        }
      }
    }
    (nodes, root)
  }


  def treeHeightNaive(n: Int, parents: List[Int]): Int = {
    var maxHeight = 0
    for (vertex <- 0 until n) {
      var height = 0
      var current = vertex
      while (current != -1) {
        //        println(current)
        height += 1
        current = parents(current)
      }
      maxHeight = maxHeight.max(height)
    }
    maxHeight
  }

  def time[R](block: => R): (R, Double) = {
    val t0 = System.currentTimeMillis()
    val result = block // call-by-name
    val t1 = System.currentTimeMillis()
    val t = t1 - t0
    println("Elapsed time: " + (t1 - t0) + "ms")
    (result, t)
  }

}
