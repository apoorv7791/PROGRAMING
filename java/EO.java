// Number to String conversion
// input num = 123
// output = one to three

public class EO {
    public static void main(String[] args) {
        int num = 123;
        String str = Integer.toString(num);
        for (int i = 0; i < str.length(); i++) {
            switch (str.charAt(i)) {
                case '1':
                    System.out.print("one ");
                    break;
                case '2':
                    System.out.println("two");
                    break;
                case '3':
                    System.out.println("three");
                    break;
                case '4':
                    System.out.println("four");
                    break;
                default:
                    System.out.print("Invalid number");
                    break;
            }
        }
    }

}
