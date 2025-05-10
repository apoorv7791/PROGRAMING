class Operation {
    int square(int n)
    {
        return n*n;
    }
    int cube(int n)
    {
        return n*n*n;
    }
}
class Cricle{
    Operation op = new Operation();
    double pi = 3.14;
    double area(int radius)
    {
        int rsquare = op.square(radius);
        return pi * rsquare;
    }
    double volume()
    {
        return (op.cube(5));
    }
    public static void main(String[] args) {
        Cricle c = new Cricle();
        double result = c.area(5);
        System.out.println(result);
        double result1 = c.volume();
        System.out.println(result1);
    }
}