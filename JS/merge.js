// how to reverse an integer number
let num = 1234;
let rev = 0;
while (num > 0) {
    let rem = num % 10;
    rev = rev * 10 + rem;
    rem = num / 10;
    num = parseInt(num / 10);
}
console.log("Number is " + num + " reversed number is " + rev);