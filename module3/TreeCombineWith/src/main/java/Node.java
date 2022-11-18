public class Node {

    public int val;
    public Node left;
    public Node right;

    public Node(int val){
        this.val = val;
    }

    public Node(int val, Node left, Node right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    public boolean isLeaf(){
        return this.left == null && this.right == null;
    }

    @Override
    public boolean equals(Object o){
        // YOUR CODE HERE
        // from epl drive
        //On appelle sur un node dont on sait qu'il n'est pas null
        //Vérifier que c'est bien le cas pour o
        if (o== null || !(o instanceof Node)){
            return false;
        }

        Node other = (Node) o;

        if(isLeaf() && other.isLeaf()){
            return val == other.val;

        }else if(!isLeaf() && !other.isLeaf()){

            if(left == null ){
                return other.left == null;
            } else if(other.left == null || !(left.equals(other.left)) ){

                return false;

            }

            if(right == null){

                return other.right == null;
            } else if(other.right == null || !(right.equals(other.right))){
                return false;
            }

            return true;

        }else {
            return false;
        }

    }
}
