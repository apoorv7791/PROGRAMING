import java.util.Scanner;
public class area {
    double length, breadth;
    double a;
    Scanner sc = new Scanner(System.in);
    void get(){
        System.out.println("Enter length :");
        length = sc.nextDouble();
        System.out.println("Enter the breadth :");
        breadth = sc.nextDouble();
        a = length * breadth;
    }
    void show(){
        System.out.println("Length is :"+ length);
        System.out.println("Breadth is :"+ breadth);
        System.out.println("Area of the rectangle is :"+a);
    }
    public static void main(String args[]){
        area a1 = new area();
        a1.get();
        a1.show();
    }
}
