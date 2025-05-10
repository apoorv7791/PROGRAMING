// program to sort an array using bubble sort
// the algorithm works by comparing each element with the next element and swapping them if they are in the wrong order
// the time complexity of the bubble sort is O(n^2) in the worst case
// the space complexity of the bubble sort is O(1) because it uses a constant amount of extra space
public class Strike {
    public static void main(String[] args) {
        int[] arr = { 50, 64, 33, 32, 22, 11, 44 };
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        System.out.println("Sorted array: " + java.util.Arrays.toString(arr));
    }
}
