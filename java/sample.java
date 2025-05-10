public class sample {
    static void fun()
    {
        System.out.println("Static methods can be called creating objects");
    }
    void get()
    {
        System.out.println("public methods must be called creating objects");
    }
    public static void main(String[] args) {
        fun();
        //get();
        sample s = new sample();
        s.get();
    }
}
