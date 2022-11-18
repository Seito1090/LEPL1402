import java.util.List;
import java.util.Stack; // this should give you a hint for the iterative version

public class Traversal {

    public static void recursiveInorder(Node root, List<Integer> res) {
        // YOUR CODE HERE
        if (root.left != null) {
            recursiveInorder(root.left, res);
        }
        res.add(root.val);
        if (root.right != null) {
            recursiveInorder(root.right, res);
        }
    }


    public static void iterativeInorder(Node root, List<Integer> res){
        // YOUR CODE HERE
        Stack<Node> stack = new Stack<>();
        Node current = root;
        while (current != null || !stack.isEmpty()){
            while (current != null){
                stack.push(current);
                current = current.left;
            }
            current = stack.pop();
            res.add(current.val);
            current = current.right;
        }
    }

}
