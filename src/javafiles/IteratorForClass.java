package javafiles;
import java.util.ArrayList;
import java.util.Iterator;

public class IteratorForClass implements Iterable<Books> {
    ArrayList<Books> a = new ArrayList<>();
    @Override
    public Iterator<Books> iterator() {
        return new BookIterator();
        // throw new UnsupportedOperationException("Unimplemented method 'iterator'");
    }
    private class BookIterator implements Iterator<Books>{
        int index = 0;
        @Override
        public boolean hasNext() {
            return a.size() != this.index;
            
            // throw new UnsupportedOperationException("Unimplemented method 'hasNext'");
        }

        @Override
        public Books next() {
            Books b = a.get(this.index);
            this.index++;
            return b;
            // throw new UnsupportedOperationException("Unimplemented method 'next'");
        }

    }
    void addBook(Books b){
        a.add(b);
    }
    
}
class Books{
    String bookName;
    String author;
    Books(String name, String author){
        this.bookName = name;
        this.author = author;
    }

    @Override
    public String toString() {
        return this.bookName + ", " + this.author;
    }
   
}
