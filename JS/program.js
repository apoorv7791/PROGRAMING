let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; // array
let evensum = 0; // sum of even numbers
let oddsum = 0; // sum of odd numbers
let sum = 0; // sum
for (let i = 0; i < array.length; i++) { // loop
    if (array[i] % 2 == 0) { // if numbers in array is even
        evensum += array[i]; // add to evensum
    }
    else { // if numbers in array is odd
        oddsum += array[i]; // add to oddsum
    }
    sum += array[i]; // add to sum
}
console.log("Sum is:" + sum);
console.log("Sum of even numbers is:" + evensum);
console.log("Sum of odd numbers is:" + oddsum);