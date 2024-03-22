package javafiles.filehandling;
import java.io.FileWriter;
import java.io.IOException;
public class WritingInFile {
    public static void main(String[] args){
        try{
            FileWriter writer = new FileWriter("src/javafiles/filehandling/created_file.txt",true);
            writer.write("Welcome to my repository.");
            writer.close();
        }catch(IOException e){

        }
        
    }
}
