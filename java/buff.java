import java.io.FileWriter;
import java.io.IOException;
class buff
{
    public static void main(String[] args) throws IOException {
        String str = "Creating a file in java "+"Using FileWriter and File Reader";
        FileWriter fw = new FileWriter("Hello.txt");
        for(int i=0; i < str.length(); i++)
        {
            fw.write(str.charAt(i));
        }
        System.out.println("File Created Sucessfully");
        fw.close();
    }
}