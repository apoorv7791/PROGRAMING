class wrapp{
    void run()
    {
        System.out.println("Package is wrapped");
    }
}
class foil extends wrapp{
    void run()
    {
        System.out.println("Only 60 Packages wrapped");
    }
    public static void main(String[] args) {
        wrapp w = new foil(); //upcasting
        w.run();
    }
}