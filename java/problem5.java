// palindrome of a number using recursion
public class problem5 {
    public static int palindrome(int n) {
        // base case
        if (n == 0) {
            return 0;
        }
        // recursive call
        return palindrome(n / 10) + n % 10;
    }

    public static void main(String[] args) {
        int n = 1212;
        palindrome(n);
    }
}
