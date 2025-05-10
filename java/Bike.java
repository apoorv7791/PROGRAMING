//Examle of an abstract class that has abstract and non abstract methods
abstract class Bike {
    Bike()
    {
        System.out.println("Bike is Created");
    }
    abstract void run();
    void changegear()
    {
        System.out.println("Gear is changed");
    }    
}
//creating a chidl class which extends the abstract class 
class Honda extends Bike{
    void run()
    {
        System.out.println("Running Safely");
    }
}
//creating a testAbstractin class to call both the abstract and non abstract methods
class TestAbstraction{
    public static void main(String[] args) {
        Bike obj = new Honda();
        obj.run();
        obj.changegear();
    }
}