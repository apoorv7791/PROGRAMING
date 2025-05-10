public class herit {
    void drink()
    {
        System.out.println("User is drinking");
    }
}
class drag extends herit{
    void repeat()
    {
        System.out.println("Process is being reapeated");    
    }
}
class remember extends drag{
    void end()
    {
        System.out.println("Process has been completed");
    }
}
class TestInherit{
    public static void main(String[] args) {
        remember r = new remember();
        r.drink();
        r.repeat();
        r.end();
    }
}
