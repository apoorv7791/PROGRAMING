public class problem3 {
    public static void find(int n, int[] arr) {
        // base case
        if (n == 0) {
            return;
        }
        if (n % 2 == 0) {
            arr[1] = arr[1]++;
        } else {
            arr[0] = arr[0]++;

        }
        // recursive case
        find(n - 1, arr);

    }

    public static void main(String[] args) {
        int[] arr = { 3, 4 };
        find(10, arr);
        System.out.println("ODd: " + arr[0]);
        System.out.println("Even: " + arr[1]);
    }
}