// program to make a calculator
let num1 = 10;
let num2 = 20;
let operation = "div";

let result;
switch (operation) {
    case "add":
        result = num1 + num2;
        break;
    case "sub":
        result = num1 - num2;
        break;
    case "mul":
        result = num1 * num2;
        break;
    case "div":
        result = num1 / num2;
        break;
    case "mod":
        result = num1 % num2;
        break;
    default:
        console.log("Invalid operation");
        break;
}

if (result !== undefined) {
    console.log(result);
}