import java.util.Scanner;

class ar {
    public static void main(String args[]) {
        int i, n;
        int arr[] = new int[50];
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter the number of elements :");
            n = sc.nextInt();
            System.out.println("Enter the elements :");
            for (i = 1; i <= n; i++) {
                arr[i] = sc.nextInt();
            }
        }
        System.out.println("Elements are :");
        for (i = 1; i <= n; i++) {
            System.out.print(arr[i]);
        }
    }
}