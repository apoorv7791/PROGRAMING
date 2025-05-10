// second largest elmeent in the array
public class Largest {
    public static void main(String[] args) {
        int[] array = { 45, 77, 55, 44, 88 };
        int max = 0;
        int secondMax = 0;
        for (int i = 0; i < array.length; i++) {
            if (array[i] > max) {
                array[i] = array[max];
            }
        }
        for (int j = 0; j < array.length; j++) {
            if (array[j] > secondMax) {
                secondMax = array[j];
            }
            System.out.println("Second Largest element is :" + secondMax);
            System.out.println("Largest element is : " + max);
        }
    }
}
