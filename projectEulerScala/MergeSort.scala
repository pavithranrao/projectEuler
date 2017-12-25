object MergeSort {
  // Courtesy : https://gist.github.com/fancellu/5e00336840098c194551
  def main(args: Array[String]): Unit = {
    val list = List(1, 4, 6, 2, 7)
    println(s"Before Sort : ${list.mkString(", ")}")

    //    val head :: tail = list
    
    val answer = mergeSort(list)
    println(s"After Sort : ${answer.mkString(", ")}")
  }

  def merge(left: List[Int], right: List[Int]): List[Int] = {
    (left, right) match {
      case (_, Nil) => left

      case (Nil, _) => right

      case (leftHead :: leftTail, rightHead :: rightTail) =>
        if (leftHead < rightHead) {
          leftHead :: merge(leftTail, right)
        }
        else {
          rightHead :: merge(left, rightTail)
        }

      //      case _ if left.head < right.head =>
      //        left.head :: merge(left.tail, right)
      //
      //      case _ if right.head < left.head =>
      //        right.head :: merge(left, right.tail)
    }
  }

  def mergeSort(list: List[Int]): List[Int] = {

    val n = list.length / 2
    if (n == 0) {
      list
    }
    else {
      val (left, right) = list.splitAt(n)
      merge(mergeSort(left), mergeSort(right))
    }
  }

}

