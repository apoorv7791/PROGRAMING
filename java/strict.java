public class strict {
    int a;
    int b;
    strict(int x, int y)
    {
        this.a=x;
        this.b=y;
    }
    int divide()
    {
        int res = a/b;
        return res;
    }
    int add()
    {
        int res = a + b;
        return res;
    }
    int multiply()
    {
        int res = a * b;
        return res;
    }
    int subtract()
    {
        int res = a - b;
        return res;
    }
    public static void main(String[] args) {
        strict s1 = new strict(45, 7);
        System.out.println("Addition is :"+s1.add());
        System.out.println("Subtraction is :"+s1.subtract());
        System.out.println("Division is :"+s1.divide());
        System.out.println("Multiplication is :"+s1.multiply());
    }
}
