// factorial of a number using recursion
public class program6 {
    public static int factorial(int n) {
        // base case
        if (n == 0) {
            return 1;
        }
        // recursive case
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        int n = 5;
        System.out.println(factorial(n)); // 120
    }
}
