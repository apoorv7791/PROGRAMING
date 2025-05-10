// reverse the array with using reecursion
public class ReverseArray {
    public static void Reverse(int[] arr, int start, int end) {
        // base case
        if (start >= end) {
            return;
        }
        // recursive case
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        Reverse(arr, start + 1, end - 1);
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5 };
        Reverse(arr, 0, arr.length - 1);
        System.out.println("Reversed array: " + java.util.Arrays.toString(arr));
    }
}
