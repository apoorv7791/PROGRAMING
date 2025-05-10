abstract class series{
    series()
    {
        System.out.println("Series is showned");
    }
    abstract void show();
    void watch()
    {
        System.out.println("Series is being watched by viewers");
    }
}
class got extends series{
    void show()
    {
        System.out.println("Rating has showned");
    }
}
class TestSeries{
    public static void main(String[] args) {
        series s = new got();
        s.watch();
        s.show();
    }
}