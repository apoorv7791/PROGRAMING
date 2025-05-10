// program to find power of a number by using recursion
// input 2 3
// output 8 (2*2*2)
public class problem4 {
    public static int power(int n, int p) {
        // base cases
        if (p == 0) {
            return 1;
        }
        // recursive case
        return n * power(n, p - 1); // recursive call of the method in the form of n - 1
    }

    public static void main(String[] args) {
        int n = 5;
        int p = 2;
        System.out.println(power(n, p)); // 25
    }
}