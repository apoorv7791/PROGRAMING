// program to find the largest number in an array
let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let max = arr[0];
let min = arr[0];

for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max) {
        max = arr[i];
    } else {
        min = arr[i];
    }
}
console.log("Maximum number is :" + max);
console.log("Minimum number is :" + min);