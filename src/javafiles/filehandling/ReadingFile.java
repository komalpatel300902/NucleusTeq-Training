package javafiles.filehandling;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadingFile {
    public static void main(String[] args){
        File obj = new File("./src/javafiles/filehandling/names.txt");
        System.out.println("file object got");
        try{
            Scanner sc = new Scanner(obj);
            while(sc.hasNextLine()){
                System.out.println(sc.nextLine());
            }
            sc.close();
        }catch(FileNotFoundException f){

        }
    }
    
}
