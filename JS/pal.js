// check if a string is palindrome or not
// input string
// palindrome : a palindrome is used to read a string or an integer is same as forward and backward

// use the two pointer technique

let str = "racecar";
let left = 0;
let right = str.length - 1;

while (left < right) {
    if (str[left] !== str[right]) {
        console.log("Not a palindrome");
        break;
    }
    else {
        console.log("It is a palindrome");
    }
    left++;
    right--;
}
