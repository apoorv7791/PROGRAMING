interface inter{
    final int a = 10;
    void display();
}
class TestInt implements inter{
    public void display()
    {
        System.out.println("Hello");
    }
    public static void main(String[] args) {
        TestInt i = new TestInt();
        i.display();
        System.out.println(i);
    }
}