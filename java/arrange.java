import java.util.Scanner;
class arrange{
    public static void main(String[] args) {
        int i, j, rows;
        Scanner s = new Scanner(System.in);
        System.out.println("Enter the number of rows :");
        rows = s.nextInt();
        for(i = 0; i <= rows; i++)
        {
            for(j = 0; j <= i; j++)
            {
                System.out.print("*" + " ");
            }
            System.out.println("");
        }
        for(i = rows-1; i >= 0; i--)
        {
            for(j = 0; j <= i-1; j++)
            {
                System.out.print("*" + " ");
            }
            System.out.println("");
        }
    }
}