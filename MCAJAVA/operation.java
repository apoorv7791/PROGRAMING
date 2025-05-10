// pow(x,y)
// // pow(x,y) = x^y
// // pow(x,y) = x*x*x...y times

class Operation {
    public static void main(String[] args) {
        int x = 2;
        int n = 3;
        System.out.println(pow(x, n));
    }

    static int pow(int x, int n) {
        if (n == 0) {
            return 1;
        }
        return x * pow(x, n - 1);
    }
}