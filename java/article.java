import java.util.Arrays;

public class article {
    public static void main(String[] args) {
        // an array with integer type elements
        int[] arr = {1,2,3,4,5,6};
        // a variable start with initial value 0
        int start = 0;
        // end variable will check the length from positive to negative length
        int end = arr.length - 1;
        // checking if the initial value of the start is less than the end
        while (start < end) {
            // a temp variable will store elements for swapping
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start ++; // start will increment the value when reversing it
            end --; // end will decrement the lower elements
        }
        System.out.println("Reversed Elements: "+ Arrays.toString(arr));

    }
}
