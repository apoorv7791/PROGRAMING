import java.util.Scanner;
public class factorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a non negative integer: ");
        int num = sc.nextInt();

        if (num < 0) {
            System.out.println("Error: number must be non negtative: ");
        }
        else {
            long factorial = 1;
            for(int i = 1; i <= num; i++){
                factorial *= i;
            }
            System.out.println("Factorial of the number is :" + factorial);
        }
        sc.close();
    }
    
}
