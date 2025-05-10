import java.util.Scanner;
class user {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter name :");
        String n = sc.nextLine();
        System.out.println("Name is :" + n);
        sc.close();
    }       
}
