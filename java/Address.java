class Address{
    String city, state, country;
    Address(String city, String state, String country)
    {
        this.city = city;
        this.state = state;
        this.country = country;
    }
}
class Emp{
    int id;
    String name;
    Address address;
    public Emp(int id, String name, Address address)
    {
        this.id = id;
        this.name = name;
        this.address = address;
    }
    void display()
    {
        System.out.println(id+" "+name);
        System.out.println(address.city+" "+address.state);
    }
    public static void main(String[] args) {
        Address a1 = new Address("gzb","UP","India");
        Address a2 = new Address("gno","UP","India");

        Emp e1 = new Emp(111, "varun",a1);
        Emp e2 = new Emp(112, "arun",a2);

        e1.display();
        e2.display();     
    } 
        
}
