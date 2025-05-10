abstract class bank {
    abstract int gateRateOfIterest();
}
class SBI extends bank{
    int gateRateOfIterest()
    {
        return 7;
    }
}
class PNB extends bank{
    int gateRateOfIterest()
    {
        return 8;
    }
}
class TestBank{
    public static void main(String[] args) {
        bank b;
        b = new SBI();
        System.out.println("Rate of Interest is :"+b.gateRateOfIterest()+"%");
        b = new PNB();
        System.out.println("Rate of Interest is :"+b.gateRateOfIterest()+"%");
     
    }
}