// word GOOGLE
// if the first and the fourth leter of the word is swapped do they remain same?
// if yes print yes else print no

let word = ["G", "O", "O", "G", "L", "E"];
let start = 0;
let end = word.length - 1;

while (start < end) {
    let temp = word[start];
    word[start] = word[end];
    word[end] = temp;
    start++;
    end--;
}
console.log(word);
if (word[0] == word[3] && word[1] == word[4] && word[2] == word[5]) {
    console.log("Yes" + word);
} else {
    console.log("No" + word);
}
// output : YesGOOGLE