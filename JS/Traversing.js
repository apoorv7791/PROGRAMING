// adding elements to an existing array
let array = [1, 2, 3, 4, 5];
array.push(6);
console.log(array); // Output: [1, 2, 3, 4, 5, 6]

// removing elements from an existing array
let array1 = [1, 2, 3, 4, 5];
array.pop();
console.log(array1); // Output: [1, 2, 3, 4]

// how can i merge the array
let newArray = [...array, ...array1];
console.log(newArray);