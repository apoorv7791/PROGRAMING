public class tr {
    int myear;
    String mname;
    tr(int year, String name) // constrcutor with paramters
    {
        myear = year;
        mname = name;
    }
    public static void main(String[] args) {
        tr c = new tr(1967, "Mustang");
        System.out.println(c.myear+ " "+c.mname);
    }
}
