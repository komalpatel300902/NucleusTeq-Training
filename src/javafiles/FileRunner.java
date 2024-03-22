package javafiles;
import java.util.Iterator;

public class FileRunner {
    public static void main(String[] args){
        IteratorForClass i = new IteratorForClass();
        Books b1 = new Books("Boy who Loved", "Durjoy Datta");
        Books b2 = new Books("The girl of my dream","Durjoy Datta");
        Books b3 = new Books("The Touch of eternity", "Durjoy Datta");
        i.addBook(b1);
        i.addBook(b2);
        i.addBook(b3);

        Iterator<Books> it = i.iterator();
        while(it.hasNext()){
            System.out.println(it.next());
        }
        try{
            System.out.println(it.hasNext());
            System.out.println(it.next());
        }catch(IndexOutOfBoundsException e){
            System.out.println(e.getClass());
            System.out.println(e.getMessage());
            System.out.println(e.getLocalizedMessage());

        }
        
    }
}
