// fibonacci number using recursion

public class Fibr {
    public static int fibonacci(int n) {
        // base case
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        // recursive case
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {
        System.out.println(fibonacci(10)); // 5
    }
}
