// program to sort the array using insertion sort
// input 50 30 20 10 40
// output 10 20 30 40 50
// the algorrithm works by inserting the elements in the correct position and splitting the array into two parts
// the left part is sorted and the right part is unsorted
// we take the first element from the unsorted part and insert it into the correct position in the sorted part
// we repeat this process until the unsorted part becomes empty
// the time complexity of the insertion sort is O(n^2) in the worst case
// the space complexity of the insertion sort is O(1)
public class Strike3 {
    public static void main(String[] args) {
        int[] array = { 50, 30, 20, 10, 40 };
        int n = array.length;
        for (int i = 0; i < n; i++) {
            int insertIndex = i;
            int currentElement = array[i];
            int j = i - 1;
            while (j >= 0 && array[j] > currentElement) {
                array[j + 1] = array[j];
                insertIndex = j;
                j--;
            }
            array[insertIndex] = currentElement;
            System.out.println("Sorted array: " + java.util.Arrays.toString(array));
        }
    }
}