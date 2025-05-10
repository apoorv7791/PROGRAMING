// check a given string is palindrome
public class Pal {
    public static void main(String[] args) {
        String s = "malyalam"; // the given string is malayalam can be read as same as forward and backward
        String rev = "";
        for (int i = s.length() - 1; i >= 0; i--) { // we traversed the string because it needed to be checked if the
                                                    // length of the string is greater than the count
            rev = rev + s.charAt(i);
        }
        if (rev.equals(rev)) {
            System.out.println("String is palindrome");
        } else {
            System.out.println("String is not palindrome");
        }
    }
}
