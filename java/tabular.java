// program to print a  multiplication table

import java.util.Scanner;

class tabular {
    public static void main(String[] args) {
        int num;
        int i;
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter the number");
            num = sc.nextInt();
            for (i = 1; i <= 10; i++) {
                System.out.println(num + " x " + i + " = " + num * i);
            }
            sc.close();
        }
    }
}
