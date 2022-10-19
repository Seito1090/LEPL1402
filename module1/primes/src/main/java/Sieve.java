import java.util.BitSet;


public class Sieve{
    
    public static BitSet bits; //You should work on this BitSet
    
    public static int numberOfPrime(int n){
        //TODO By Student
        bits = new BitSet(n);
        bits.flip(2, n);

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (bits.get(i)) {
                for (int j = 2 * i; j < n; j += i) {
                    bits.set(j, false);
                }
            }
        }
        return bits.cardinality();
    }

    public static void main(String[] args) {
        int test = numberOfPrime(100);
        System.out.println(test);
    }
}

