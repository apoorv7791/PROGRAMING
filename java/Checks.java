// search an element in array find all occurrences
// input 10 20 30 40 50 50
// output 50 is found at index 4 and 5 
// use recursion
public class Checks {
    public static int search(int[] arr, int n, int i, int x) {
        // base case
        if (i == n) {
            return -1;
        }
        // recursive case
        if (arr[i] == x) {
            return i;
        } else {
            return search(arr, n, i + 1, x);
        }
    }

    public static void main(String[] args) {
        int[] arr = { 10, 20, 30, 40, 50, 50 };
        int n = arr.length;
        int x = 50;
        int i = 0;
        int result = search(arr, n, i, x);
        if (result == -1) {
            System.out.println("Element not found");
        } else {
            System.out.println("Element found at index " + result);
        }
    }
}
