// program to remove duplicate elements from an array
// input 1 2 2 3 4 4 5
// output 1 2 3 4 5
class num {
    public static void main(String[] args) {
        int arr[] = { 1, 2, 2, 3, 4, 4, 5 };
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] == arr[j]) {
                    count++;
                } else {
                    continue;
                }
                if (count == 0) {
                    System.out.println(arr[i]);
                } else {
                    count--;
                    break;
                }
            }
        }
    }
}