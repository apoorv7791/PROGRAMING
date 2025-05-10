function BubbleSort(array) {
    let n = array.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                let temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
    return array;
}
let array = [3, 1, 4, 2, 5, 11, 0, 10, 6, 9, 8, 12];

console.log("Sorted array is: " + BubbleSort(array));