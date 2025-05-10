public class sceret {
    int rollno;
    String name;
    static String  college = "IITM";
    sceret(int r, String n) // constructor 
    {
        rollno = r;
        name = n;
    }
    void display()
    {
        System.out.println(rollno+" "+name+" "+college);
    }
            public static void main(String[] args) {
            sceret s1 = new sceret(1, "karan");
            sceret s2 = new sceret(12, "Ravi");
            s1.display();
            s2.display();
        }
    }

