public class pat {
    public static void main(String agrs[]){
        int i, n=4, j, k=1;
        for(i=0; i<=n; i++){
            for(j=0; j<=i; j++){
                System.out.print(" "+k);
                k++;
            }
            System.out.println();
        }
    }
}
