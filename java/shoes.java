abstract class shoes {
    abstract int buy();    
}
class  Nike extends shoes{
    int buy()
    {
        return 5000;
    }
}
class Jordan extends shoes{
    int buy()
    {
        return 8000;
    }
}
class TestShoes{
    public static void main(String[] args) {
        shoes s;
        s = new Nike();
        System.out.println("Cost of Nike is :"+s.buy());
        s = new Jordan();
        System.out.println("Cost of jordan is :"+s.buy());
    }
}