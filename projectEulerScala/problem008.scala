object Solution {
   def main(args: Array[String]) {

     def max(x : Int, y : Int) = {
       if(x > y){
         x
       }else{
         y
       }
     }

     def getMaxProd(x : String, slide : Int) : Int = {
       x.toCharArray.map(_ - 48).sliding(slide).foldLeft(0)((x,y) => max(x, y.product))
     }

     val sc = new java.util.Scanner(System.in)
     val t = sc.nextInt()
     for (idx <- 0 to t) {
       sc.nextInt()
       val k = sc.nextInt()
       val num = sc.next()
       println(getMaxProd(num, k))
     }
  }
}
