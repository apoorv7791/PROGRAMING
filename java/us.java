import java.util.Scanner;
class explain{
    String name;
    int age;
    String Address;
    Scanner s =  new Scanner(System.in);
    void input()
    {
        System.out.println("Enter your name :");
        name = s.nextLine();
        System.out.println("Enter age :");
        age = s.nextInt();
        System.out.println("Enter address :");
        Address = s.next();
    }
    void display()
    {
        System.out.println("Name is :"+name);
        System.out.println("Age is :"+age);
        System.out.println("Address is :"+Address);
    }
    public static void main(String args[]) {
        explain e = new explain();
        e.input();
        e.display();
    }
}