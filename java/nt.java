import java.util.Scanner;
public class nt {
    String name;
    int age;
    String address;
    Scanner s = new Scanner(System.in);
    void get()
    {
        System.out.println("Enter your name :");
        name = s.nextLine();
        System.out.println("Enter your age :");
        age = s.nextInt();
        System.out.println("Enter your address :");
        address = s.next();
    }
    void show()
    {
        System.out.println("Name is :"+name);
        System.out.println("Age is :"+age);
        System.out.println("Address is :"+address);
    }
    public static void main(String[] args) {
        nt n = new nt();
        n.get();
        n.show();
    }
}
