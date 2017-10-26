object Solution {
   val primes: Stream[Int] = 2 #:: Stream.from(3, 2).filter(isPrime)

   def isPrime(n: Int): Boolean = {
    primes.takeWhile(p => p * p <= n).forall(n % _ != 0)
   }
   def main(args: Array[String]) {

    val sc = new java.util.Scanner (System.in);
        var t = sc.nextInt()
        for(i  <- 0 until t){
          var n = sc.nextInt()
          println(primes(n - 1))
        }
   }
}
