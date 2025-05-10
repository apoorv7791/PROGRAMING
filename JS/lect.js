// program to implement selection sort in an unsorted array
array = [64, 25, 12, 22, 11];
let n = array.length;
for (let i = 0; i < n; i++) {
    let min = i;
    for (let j = i + 1; j < n; j++) {
        if (array[j] < array[min]) {
            min = j;
        }
    }
    if (min !== i) {
        let temp = array[i];
        array[i] = array[min];
        array[min] = temp;
    }
}
console.log("Sorted array is: " + array);