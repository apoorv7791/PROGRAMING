import java.util.Scanner;
class student{
    String name;
    int age;
    Scanner sc = new Scanner(System.in);
    void input(){
        System.out.println("Enter name :");
        name = sc.nextLine();
        System.out.println("Enter age :");
        age = sc.nextInt();
    }
}
class marks extends student{
    double m1, m2;
    double total;
    Scanner s = new Scanner(System.in);
    void get(){
        System.out.println("Enter first marks :");
        m1 = s.nextDouble();
        System.out.println("Enter seocnd marks :");
        m2 = s.nextDouble();
        total = m1 + m2;
    }
    void display(){
        System.out.println("Name is :"+ name);
        System.out.println("Age is :"+ age);
        System.out.println("First makrs are :"+ m1);
        System.out.println("Seocnd marks are :"+ m2);
        System.out.println("Total marks are :"+ total);
    }
    public static void main(String args[]){
        marks m = new marks();
        m.input();
        m.get();
        m.display();
    }
}