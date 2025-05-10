import java.util.Scanner;
class tab{
    public static void main(String[] args) {
        int i, n;
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter the number");
            n = sc.nextInt();
        }
        for(i=1; i<=10; i++){
           System.out.println(n+ " x " +i+ " = " +n*i); 
        }
    }
}