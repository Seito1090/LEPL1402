import java.util.Stack;
import java.util.NoSuchElementException;

public class MyQueue<E> {

    Stack<E> s1;
    Stack<E> s2;

    private E front;

    /*
     * Constructor
     */
    public MyQueue() {
        s1 = new Stack<>();
        s2 = new Stack<>();
        this.front = null;
    }

    /**
     * Add an element to the end of the list
     *
     * @param elem The element to add
     */
    public void enqueue(E elem) {
        // TODO
        s1.push(elem);
        if(front == null){
            front = elem;
        }
    }

    /**
     * Remove the first element from the queue
     *
     * @return The oldest element in the queue
     * @throws NoSuchElementException if the queue is empty
     */
    public E dequeue() {
        // TODO
        if (s1.empty()){
            throw new NoSuchElementException();
        }
        E elem;
        while (!s1.empty()) {
            s2.push(s1.pop());
        }
        elem = s2.pop();
        if(!s2.empty()) {
            front = s2.peek();
        } else {
            front = null;
        }
        while(!s2.empty()){
            s1.push(s2.pop());
        }
        return elem;
    }

    /**
     * Peek at the first element of the queue
     *
     * @return The first element of the queue
     * @throws NoSuchElementException if the queue is empty
     */
    public E peek() {
        // TODO
        if (this.front == null) {
            throw new NoSuchElementException();
        }
        return this.front;
    }

    /**
     * @return true if the queue is empty
     */
    public boolean empty() {
        // TODO
        return s1.empty();
    }

}
