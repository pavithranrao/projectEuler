package org.euler.problem

import scala.annotation.tailrec

object Problem003 {

  def sqrt(number: BigInt): BigInt = {
    def next(n: BigInt, i: BigInt): BigInt = (n + i / n) >> 1

    val one = BigInt(1)
    val n = one
    val n1 = next(n, number)

    @tailrec
    def sqrtHelper(n: BigInt, n1: BigInt): BigInt =
      if ((n1 - n).abs <= one) {
        List(n1, n).max
      }
      else {
        sqrtHelper(n1, next(n1, number))
      }

    sqrtHelper(n, n1)
  }

  def main(args: Array[String]): Unit = {

    // Courtesy : https://medium.com/coding-with-clarity/functional-vs-iterative-prime-numbers-in-scala-7e22447146f0
    def calculatePrimesStream(end: Int): List[Int] = {
      val odds = Stream.from(3, 2).takeWhile(_ <= Math.sqrt(end).toInt)
      val composites = odds.flatMap(i => Stream.from(i * i, 2 * i).takeWhile(_ <= end))
      Stream.from(3, 2).takeWhile(_ <= end).diff(composites).toList
    }

    val inputArray = Array(BigInt("600851475143"), BigInt("700851475143"))
    val maxInput = inputArray.max
    val primeList = calculatePrimesStream(sqrt(maxInput).toInt).reverse

    inputArray.foreach { input =>
      println(s"input and the sqrt of input is : $input , ${sqrt(input)}")

      val answer = primeList
        .find(input % _ == 0)
      println(answer.get)

    }

  }

}

