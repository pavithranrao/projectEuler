package org.euler.problem

object Problem004 {
  def main(args: Array[String]): Unit = {
    def digits(n: Int) = n.toString.toList.map(_.asDigit)

    def isPalindrome(n: Int) = digits(n) == digits(n).reverse

    // todo : try scalaz with breakable foldLeft
    val answer = (999 to 100 by -1).flatMap {
      x =>
        (999 to 100 by -1).map {
          y =>
            x * y
        }
    }.filter(isPalindrome).max

    println(s"$answer")
  }

}
