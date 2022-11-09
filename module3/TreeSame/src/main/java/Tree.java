public class Tree {

    public Node root;

    public Tree(Node root){
        this.root = root;
    }

    @Override
    public boolean equals(Object o){
        // YOUR CODE HERE
        if (o instanceof Tree){
            Tree t = (Tree) o;
            if (this.root == null){
                return t.root == null;
            }else if (t.root == null){
                return false;
            }else{
                return this.root.equals(t.root);
            }
        }
        return false;
    }

}