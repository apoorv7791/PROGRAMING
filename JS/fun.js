// use all types of functions to calculate the factorial of a number
// simple function
function fact(n) {
    let fact = 1;
    for (let i = 1; i <= n; i++) {
        fact = fact * i;
    }
    return fact;
}
console.log(fact(6)); // result is 720


// arrow function
let factorial = (n) => {
    let factorial = 1;
    for (let i = 1; i <= n; i++) {
        factorial = factorial * i;
    }
    return factorial;
}
console.log(factorial(5));

// Anonymous function
let factOfaNumber = function (n) {
    let factOfaNumber = 1;
    for (let i = 1; i <= n; i++) {
        factOfaNumber = factOfaNumber * i;
    }
    return factOfaNumber;
}
console.log(factOfaNumber(6));