abstract class ed {
    abstract void run();
}
class red extends ed{
    void run()
    {
        System.out.println("Running smoothly");
    }
    public static void main(String[] args) {
        ed d = new red();
        d.run();
    }
}