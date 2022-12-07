public class Leaf implements Visitable {
    
    // YOUR CODE HERE
    private int value;

    public Leaf(int size) { value = size; }

    public int getValue() {
        // YOUR CODE HERE
        return value;
    }
    @Override
    public int accept(Visitor visitor){
        return value;
    }
}
