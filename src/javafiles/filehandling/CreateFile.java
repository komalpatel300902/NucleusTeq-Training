package javafiles.filehandling;
import java.io.File;
import java.io.IOException;
public class CreateFile {
    public static void main(String[] args){
        File f = new File("src/javafiles/filehandling/created_file.txt");
        try{
            if(f.createNewFile()){
                System.out.println(f.getName()+ " File created success fully");
            }
        }catch(IOException i){

        }
        
    }
}
