import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

class dis{
    public static void main(String[] args) throws IOException{
        int ch;
        FileReader f = null;
        try
        {
            f = new FileReader("text");
        }
        catch(FileNotFoundException fe)
        {
            System.out.println("File does not exist");
        }
        while((ch=f.read()) !=-1)
        {
            System.out.print((char)ch);
        }
        f.close();
    }
}