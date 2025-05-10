// Given a string s determine if it is a palindrome or not.
// A palindrome is a string that is the same forwards and backwards.
// For example, the following strings are palindromes:
// "abba"
// "racecar"
// "deified"
// "rotor"
// How to solve this problem?
// We can solve this problem using a two pointer approach.
// We can use two pointers, one starting from the beginning of the string and the other starting from the end of the string.
// We can compare the characters at the two pointers.
// If the characters are not the same, we can return false.
// If the characters are the same, we can move the two pointers towards each other.
// If the two pointers meet, we can return true.
// Let's implement the code:
class p {
    public static boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            } else {
                left++;
                right--;

            }
        }
        return true;
    }

    public static void main(String[] args) {
        String s = "racecar";
        System.out.println(isPalindrome(s)); // true
        System.out.println(isPalindrome("hello")); // false
        System.out.println(isPalindrome("deified")); // true
        System.out.println(isPalindrome("rotor")); // true

    }
}