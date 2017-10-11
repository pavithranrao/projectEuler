object Solution {
  def sumOfMultiples(n: Int): Long = {
    def sumOfAP(m: Int): Long = {
      val size = ((n - 1) / m).toLong
      m * size * (size + 1) / 2
    }
    sumOfAP(3) + sumOfAP(5) - sumOfAP(15)
  }

  def main(args: Array[String]) {
    val m = readLine.toInt
    for (i <- 1 to m) {
      val n = readLine.toInt
      println(sumOfMultiples(n))
    }
  }
}