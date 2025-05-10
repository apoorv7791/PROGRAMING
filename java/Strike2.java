// program to sort an array using selection sort
public class Strike2 {
    public static void main(String[] args) {
        int[] array = { 45, 77, 55, 44, 88 };
        for (int i = 0; i < array.length; i++) {
            int minIndex = i;
            for (int j = i + 1; j < array.length; j++) {

                if (array[i] > array[minIndex]) {
                    minIndex = j;
                }
                if (minIndex != i) {
                    int temp = array[i];
                    array[i] = array[minIndex];
                    array[minIndex] = temp;

                }
            }
        }
        System.out.println("Sorted array: " + java.util.Arrays.toString(array));
    }
}
