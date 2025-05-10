import java.util.Scanner;
class cl{
    String name;
    int age;
    String Address;
    Scanner obj = new Scanner(System.in);
    void input(){
        System.out.println("Enter your name :");
        name = obj.nextLine();
        System.out.println("Enter your age :");
        age = obj.nextInt();
        System.out.println("Enter your address :");
        Address = obj.next();
        obj.close();
    }
    void display(){
        System.out.println("Name is :"+ name);
        System.out.println("Age is :"+ age);
        System.out.println("Address is :"+ Address);
    }
    public static void main(String[] args) {
        cl c = new cl();
        c.input();
        c.display();
    }
}