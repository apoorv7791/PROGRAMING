import java.io.IOException;
import java.io.InputStreamReader;
import java.io.*;
public class read {
    public static void main(String[] args) throws IOException{
        InputStreamReader in = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(in);
        String name = "";
        while(!name.equals("stop"))
        {
            System.out.println("Enter the data");
            name = br.readLine();
            System.out.println("Entered data is :" +name);
        }
        br.close();
        in.close();
    }
}
