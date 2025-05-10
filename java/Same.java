// Program to reverse the string 
public class Same {
    public static void main(String[] args) {
        String str = "Apoorv";
        for (int i = 0; i < str.length() - 1; i++) {
            System.out.print(str.charAt(i));
        }
        System.out.println(str.charAt(str.length() - 1));
    }
}
