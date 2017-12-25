object Solution {
  

  def main(args: Array[String]) {
    val m = readLine.toInt
    for (i <- 1 to m) {
      val n = readLine.toInt
      println(sumOfMultiples(n))
    }
  }
}
