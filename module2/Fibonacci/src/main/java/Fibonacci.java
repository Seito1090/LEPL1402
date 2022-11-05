public class Fibonacci {


    public static int fiboRecursive(int index){
        //TODO HERE CODE HERE n = index
        if (index < 2 ){return index;}
        return fiboRecursive(index - 1) + fiboRecursive(index - 2);
    }


    public static int fiboIterative(int index){
        //TODO YOUR CODE HERE
        if (index < 2) {return index;}
        int a = 0;
        int b = 1;
        for (int i = 2; i <= index; i++) {
            int x = b;
            b += a;
            a = x;
        }
        return b;
    }

}
