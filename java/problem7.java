// a program to remove duplicate charcters from a astring using recursion
// input: "AAABBBCCC"
// output: "ABC"

public class problem7 {
    private static String removeDuplicates(String str) {
        // base case
        if (str.length() == 0) {
            return str;
        }
        // small problem
        String s = removeDuplicates(str.substring(1));
        // recursive case
        if (str.charAt(0) != s.charAt(0)) {
            return str.charAt(0) + s;
        } else {
            return s;
        }
    }

    public static void main(String[] args) {
        String str = "AAABBBCCC";
        String result = removeDuplicates(str);
        System.out.println(result);
    }
}
