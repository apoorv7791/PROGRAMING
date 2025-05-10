// program to print fibonacci series
let num = 10;
let a = 0;
let b = 1;
for (let i = 0; i < num; i++) {
    console.log(a);
    let c = a + b;
    a = b;
    b = c;
}
console.log("Fibonacci Series upto " + num + " is: " + a);  // Output: Fibonacci Series upto 10 is: 55