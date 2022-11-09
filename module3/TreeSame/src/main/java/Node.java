public class Node {

    public int val;
    public Node left;
    public Node right;

    public Node(int val){
        this.val = val;
    }

    public boolean isLeaf(){
        return this.left == null && this.right == null;
    }

    @Override
    public boolean equals(Object o){
        // YOUR CODE HERE
        // don't have to check for null object cuz we only pass in Node objects
        Node compare = (Node) o;
        if (compare.isLeaf() && this.isLeaf()){
            return compare.val == this.val;
        } else if (!compare.isLeaf() && !this.isLeaf()){
            return compare.val == this.val && compare.left.equals(this.left) && compare.right.equals(this.right);
        }
        return false;
    }
}