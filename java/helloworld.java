// program to reveerse a given number
// input  123
// output 321
class helloworld {
    public static void main(String[] args) {
        int num = 123;
        int rev = 0;
        while (num != 0) {
            int rem = num % 10;
            rev = rev * 10 + rem;
            num = num / 10;
        }
        System.out.println("Reveersed number is: " + rev);

    }
}