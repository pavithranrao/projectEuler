object Solution {

    val primes: Stream[Int] = 2 #:: Stream.from(3, 2).filter(isPrime)

    def isPrime(n: Int): Boolean = {
       primes.takeWhile(p => p * p <= n).forall(n % _ != 0)
    }

    def getLogOfBaseN(n: Double, b: Int): Double = Math.log(n) / Math.log(b)

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var t = sc.nextInt()
        for(i  <- 0 until t){
            var n = sc.nextInt()
            val primesN = primes.takeWhile(_ <= n).toList

            val answer = primesN.foldLeft(BigInt(1)) {
              (prod, number) =>
                val maxPower = getLogOfBaseN(n.toDouble, number).toInt
                prod * Math.pow(number, maxPower).toInt
          }

          println(answer)
        }
    }
}
