public class problem8 {
    private static int[] search(int[] arr, int n, int i, int x) {
        // base case
        if (i == n) {
            return new int[] { -1, 0 };
        }
        // recursive case
        if (arr[i] == x) {
            int[] result = search(arr, n, i + 1, x);
            result[1] = result[1] + 1;
            return result;
        } else {
            int[] result = search(arr, n, i + 1, x);
            return result;
        }
    }

    public static void main(String[] args) {
        int[] arr = { 10, 20, 30, 40, 50, 50 };
        int n = arr.length;
        int x = 50;
        int i = 0;
        int[] result = search(arr, n, i, x);
        System.out.println("Element found at index " + result[0] + " and " + result[1]);
    }
}
