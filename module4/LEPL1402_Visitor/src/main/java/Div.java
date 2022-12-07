public class Div extends Node implements Visitable {
    // YOUR CODE HERE
    public Div(Visitable left, Visitable right){
        super (left, right);
    }

    @Override
    public int accept(Visitor visitor) throws IllegalArgumentException{
        if (getRight().accept(visitor) == 0) throw new IllegalArgumentException();
        return getLeft().accept(visitor) / getRight().accept(visitor);
    }
}
