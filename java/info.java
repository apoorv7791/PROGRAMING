import java.util.Scanner;
public class info {
    String name;
    int age;
    String location;
    Scanner sc = new Scanner(System.in);
    void get(){
        System.out.println("Enter your name :");
        name = sc.nextLine();
        System.out.println("Enter your age :");
        age = sc.nextInt();
        System.out.println("Enter your location :");
        location = sc.next();
    }
}
class details extends info{
    String fname, mnmae;
    int fage, mage;
    Scanner s = new Scanner(System.in);
    void input(){
        System.out.println("Enter Father's name :");
        fname = s.nextLine();
        System.out.println("Enter father's age :");
        fage = s.nextInt();
        System.out.println("Enter mother's name :");
        mnmae = s.next();
        System.out.println("Enter mother's age :");
        mage = s.nextInt();
    }
    void display(){
        System.out.println("Name is :"+name);
        System.out.println("Age is :"+age);
        System.out.println("Location is :"+location);
        System.out.println("Father's name is :"+fname);
        System.out.println("Father's age is :"+fage);
        System.out.println("Mother's name is :"+mnmae);
        System.out.println("Mother's age is :"+mage);
    }
    public static void main(String args[]) {
        details d = new details();
        d.get();
        d.input();
        d.display();
    }
}
