class interconnect {
    void create()
    {
        System.out.println("Something is being created");
    }    
}
class actual extends interconnect{
    void life()
    {
        System.out.println("A life has been given to the creation");
    }
    void execute()
    {
        System.out.println("All the parts are well functioning");
    }
    public static void main(String[] args) {
        actual a = new actual();
        a.create();
        a.life();
        a.execute();
    }
}
