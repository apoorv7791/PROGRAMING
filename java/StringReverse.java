// public class StringReverse {
//     public static String reverse(String s) {
//         // base case
//         if (s.length() == 0) {
//             return s;
//         }
//         // recursive case
//         return reverse(s.substring(1)) + s.charAt(0);
//     }

//     public static void main(String[] args) {
//         String s = "hello";
//         System.out.println(reverse(s)); // olleh
//     }

// }
// can we use a two pointer approach to solve this problem?
// yes, we can use a two pointer approach to solve this problem.
// we can use the two pointer approach to reverse the string.

public class StringReverse {
    public static String reverse(String s) {
        char[] arr = s.toCharArray();
        int start = 0;
        int end = arr.length - 1;
        while (start < end) {
            char temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
        return new String(arr);
    }

    public static void main(String[] args) {
        String s = "hello";
        System.out.println(StringReverse.reverse(s)); // olleh
        System.out.println(StringReverse.reverse("Apoorv")); // vroopA
        System.out.println(StringReverse.reverse("Sachin")); // nihcaS
    }
}