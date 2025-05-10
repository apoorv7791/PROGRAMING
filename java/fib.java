class fib {
    public static void main(String[] args) {
        int n1 = 0, n2 = 1, count = 10; // variable a = 0 and variable b = 1 with a count of 10
        for (int i = 0; i < count; i++) { // loop to print the first 10 numbers
            int c = n1 + n2; // c = a + b which means the sum of a and b
            n2 = n1; // b = a
            n1 = c; // a = c
            System.out.print(c + " "); // print the value of c
        }
    }
}