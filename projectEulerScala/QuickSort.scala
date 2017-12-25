object QuickSort {

  def quickSort(array: Array[Int], start: Int, end: Int): Array[Int] = {

    if (start < end) {
      val partitionIndex = partition(array, start, end)

      quickSort(array, start, partitionIndex - 1)
      quickSort(array, partitionIndex + 1, end)
    }
    array
  }

  def partition(array: Array[Int], start: Int, end: Int): Int = {

    val pivot = array(end)
    var wall = start

    def swap(source: Int, dest: Int) {
      val temp = array(source)
      array(source) = array(dest)
      array(dest) = temp
    }

    for (idx <- start until end) {
      if (array(idx) < pivot) {
        swap(idx, wall)
        wall += 1
      }
    }
    swap(wall, end)

    wall
  }

  def main(args: Array[String]): Unit = {

    val array = Array(1, 4, 6, 2)
    println(s"Before Sort : ${array.mkString(", ")}")

    val answer = quickSort(array, 0, array.length - 1)
    println(s"After Sort : ${answer.mkString(", ")}")
  }

}

