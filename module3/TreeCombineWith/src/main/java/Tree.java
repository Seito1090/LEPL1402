public class Tree {

    public Node root;

    public Tree(Node root){
        this.root = root;
    }

    public Tree combineWith(Tree o){
        // YOUR CODE HERE
        if (o == null){
            return this;
        }
        if (this.root == null){
            return o;
        }
        if (o.root == null){
            return this;
        }
        //we create a tree to store the new values
        Tree newTree = new Tree(new Node(0));
        createTree(this.root, o.root, newTree.root);
        return newTree;
    }
    private void createTree(Node tree1, Node tree2, Node finalTree){

        // we know that the nodes are not null since we checked that in the combineWith method
        // but we have to check if the left and right leaves are null or not

        if (tree1.left != null || tree2.left != null) {

            // if either left leave in the 2 trees are not null
            //it means that we did not reach the end of the branch so we continue and add a branch to the final tree

            finalTree.left = new Node(0);
            if (tree1.left != null && tree2.left != null) {

                //if both are not null we continue recursively

                createTree(tree1.left, tree2.left, finalTree.left);
            } else if (tree1.left == null) {

                // if only one is null that means one tree is finished and we have to continue with only the other

                continueTreeBranch(tree2.left, finalTree.left);
            } else {
                continueTreeBranch(tree1.left, finalTree.left);
            }
        }
        finalTree.val = tree1.val + tree2.val;

        // we do the same for the right branch

        if (tree1.right != null || tree2.right != null){
            finalTree.right = new Node(0);
            if (tree1.right != null && tree2.right != null){
                createTree(tree1.right, tree2.right, finalTree.right);
            } else if (tree1.right == null){
                continueTreeBranch(tree2.right, finalTree.right);
            } else {
                continueTreeBranch(tree1.right, finalTree.right);
            }
        }
    }
    private void continueTreeBranch(Node Branch, Node finalTreeBranch){
        finalTreeBranch.val = Branch.val;
        if (!Branch.isLeaf()){
            if (Branch.left != null){
                finalTreeBranch.left = new Node(0);
                continueTreeBranch(Branch.left, finalTreeBranch.left);
            }
            if (Branch.right != null){
                finalTreeBranch.right = new Node(0);
                continueTreeBranch(Branch.right, finalTreeBranch.right);
            }
        }
    }
}