// program to check a number is palindrome or not

class petrol {
    public static void main(String[] args) {
        int original = 121;
        int start = original;
        int end = 0;
        while (start != 0) {
            int rem = start % 10;
            end = end * 10 + rem;
            start = start / 10;
        }
        if (end == original) {
            System.out.println("Number is palindrome");
        } else {
            System.out.println("Number is not palindrome");

        }
    }
}