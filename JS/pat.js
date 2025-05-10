// *
// **
// ***
// ****
// ***** printing pattern

let rows = 5;
let columns = 1;
for (let i = 0; i <= rows; i++) {
    for (let j = 0; j <= columns; j++) {
        process.stdout.write("*");
    }
    console.log("");
}