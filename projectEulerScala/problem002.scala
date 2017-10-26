object Solution {

  def main(args: Array[String]) {
    lazy val fibs: Stream[BigInt] = BigInt(0) #:: BigInt(1) #:: fibs.zip(fibs.tail).map { n => n._1 + n._2 }
    val sc = new java.util.Scanner(System.in)
    val t = sc.nextInt()
    for (idx <- 0 to t) {
      val n = sc.nextLong()
      val fibSum = fibs.takeWhile(_ < BigInt(n)).filter(_ % 2 == 0).sum
      println(fibSum)
    }
  }
}
