public class B{
    int RateOfInterest()
    {
        return 0;
    }
}
class S extends B{
    int RateOfInterest()
    {
        return 8;
    }
}
class I extends B{
    int RateOfInterest()
    {
        return 7;
    }
}
class A extends B{
    int RateOfInterest()
    {
        return 9;
    }
}
class TestB{
    public static void main(String[] args) {
        S s = new S();
        I i = new I();
        A a = new A();
        System.out.println("S rateofinterest :"+s.RateOfInterest());
        System.out.println("I rateofinterest :"+i.RateOfInterest());
        System.out.println("A rateofinterest :"+a.RateOfInterest());
    }
}