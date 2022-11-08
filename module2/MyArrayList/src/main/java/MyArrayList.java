import java.util.ConcurrentModificationException;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class MyArrayList<Item> implements Iterable<Item> {

    private Object [] list;
    private int size;

    public static void main(String[] args) {
        MyArrayList<Integer> simple = new MyArrayList<Integer>(5);
        simple.enqueue(1);
        simple.enqueue(2);
        simple.enqueue(3);
        simple.enqueue(4);
        simple.enqueue(5);
        Integer res = simple.remove(1); // removes "2"
    }

    public MyArrayList(int initSize) throws IndexOutOfBoundsException{
        // YOUR CODE HERE
        if (initSize < 0) {
            throw new IndexOutOfBoundsException();
        }
        list = new Object[initSize];
        size = 0;
    }


    /*
    * Checks if 'list' needs to be resized then add the element at the end 
    * of the list.
    */
    public void enqueue(Item item){
        // YOUR CODE HERE
        if (size >= list.length){
            increaseAndCopy();
        }
        list[size] = item;
        size++;
    }


    /*
    * Removes the element at the specified position in this list.
    * Returns the element that was removed from the list. You dont need to 
    * resize when removing an element.
    */
    public Item remove(int index) throws IndexOutOfBoundsException{
        // YOUR CODE HERE
        if (index < 0 || index > size){
            throw new IndexOutOfBoundsException();
        }
        Item item  = (Item) list[index];
        // don't forget the shift left the elements that came after the item you popped out :)
        for (int i = index; i < size - 1; i++){
            list[i] = list[i+1];
        }
        list[size-1] = null;
        size--;
        return item;
    }
    public void increaseAndCopy(){
        Object[] newList = new Object[list.length * 2];
        for (int i = 0; i < list.length; i++){
            newList[i] = list[i];
        }
        list = newList;
    }

    public int size(){
        return this.size;
    }
    
    
    public Object [] getList(){
        return this.list;
    }


    @Override
    public Iterator<Item> iterator() {
        return new MyArrayListIterator();
    }


    private class MyArrayListIterator implements Iterator<Item> {
        // YOUR CODE HERE
        private int initialSize = size;
        private int index = 0;

        @Override
        public void remove(){
            throw new UnsupportedOperationException();
        }
        @Override
        public boolean hasNext(){
            return index < size && concurrentCheck();
        }
        private boolean concurrentCheck(){
            if (initialSize != size){
                throw new ConcurrentModificationException();}
            return true;
        }
        @Override
        public Item next(){
            if (!hasNext()) {throw new NoSuchElementException();}
            return (Item) list[index++];
        }

    }

}