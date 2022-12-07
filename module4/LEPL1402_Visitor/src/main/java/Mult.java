public class Mult extends Node implements Visitable {
    // YOUR CODE HERE
    public Mult(Visitable left, Visitable right) {
        super(left, right);
    }
    @Override
    public int accept(Visitor visitor){
        return getLeft().accept(visitor) * getRight().accept(visitor);
    }
}
