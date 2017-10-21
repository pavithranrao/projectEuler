object Solution {
   def main(args: Array[String]) {

    def getSumOfN (n : BigInt) = (n *(n + 1))/2
    def getSumOfNSquare (n : BigInt) = (n *(n + 1) * (2*n +1))/6

    val sc = new java.util.Scanner (System.in);
        var t = sc.nextInt()
        for(i  <- 0 until t){
          var n = sc.nextInt()
          val sumOfN = getSumOfN(n)
          val answer = sumOfN*sumOfN - getSumOfNSquare(n)

          println(answer)
        }
   }
}
