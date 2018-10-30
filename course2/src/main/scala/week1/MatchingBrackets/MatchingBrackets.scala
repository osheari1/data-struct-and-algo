//package week1.MatchingBrackets

import java.util.Scanner

import scala.collection.mutable

object MatchingBrackets extends App {
  override def main(args: Array[String]): Unit = {

    val scanner = new Scanner(System.in)
    val inp = scanner.nextLine().toCharArray.toList
    val output = matchingBrackets(inp)
    if (output == -1)
      println("Success")
    else
      println(output)

//    val inps = List(
//      "[]",
//      "{}[]",
//      "[()]",
//      "(())",
//      "{[]}()",
//      "{",
//      "{[])",
//      "{[]",
//      "]()",
//      "()[}",
//      "{}([]",
//      "[](()",
//      "ablabla)ihihi(ohoho"
//
//
//      )

//    inps.foreach { inp =>
//      println(inp)
//      val output = matchingBrackets(inp.toCharArray.toList)
//      println(output)
//      println()
//    }


  }

  def matchingBrackets(inp: List[Char]): Int = {
    val start = List('(', '[', '{')
    val end = List(')', ']', '}')
    val stack = new mutable.Stack[Char]()
    val stackIx = new mutable.Stack[Int]()

    var ix = 1
    for (c <- inp) {
//            println(s"ix: $ix")
//            print(s"stack: ${stack.fold("")(_.toString + _.toString)}\t")
//            println(s"stackIx: ${stackIx.fold("")(_.toString + _.toString)}")
//            println()
      if (start.contains(c)) {
        //        println(s"")
        stack.push(c)
        stackIx.push(ix)
        ix += 1
      } else if (!end.contains(c)) {
        stackIx.push(ix)
        ix +=1
      } else {
        if (stack.isEmpty) {
          return ix
        }
        val last = stack.pop()
        val lastIx = stackIx.pop()

        if (c != end(start.indexOf(last))) {
          return ix
        }
        ix += 1
      }
    }
    if (stack.isEmpty) -1 else stackIx.pop()
  }

}
