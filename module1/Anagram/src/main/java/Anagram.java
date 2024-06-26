import java.lang.reflect.Array;

public class Anagram {

    /**
     * Count the number of occurrences of each letter of the alphabet
     * (from 'A' to 'Z') in the given string. The function must return
     * an array containing 26 elements: The item with index 0 contains
     * the number of 'A' in the string, the item with index 1 contains
     * the number of 'B', and so on.
     *
     * This function must be case-insensitive, i.e. the character 'f'
     * must be considered as the same as character 'F'.
     *
     * Characters that are neither in the range 'a' to 'z', nor in the
     * range 'A' to 'Z' must be ignored.
     * 
     * @param s The string of interest.
     * @return An array counting the number of occurrences of each
     * letter.
     **/
    public static int[] countAlphabet(String s) {
        int[] nbr = new int[26];
        s = s.toLowerCase();
        for (int i = 0; i < s.length(); i++) {
            int val = (int) s.charAt(i);
            if (val < 97 || val > 123){
                continue;
            } else {
                nbr[val-97]++;
            }

        }
        return nbr;
    }


    /**
     * Check whether one string is an anagram of another string. It is
     * strongly advised to use the function "countAlphabet()" as a
     * building block for function "isAnagram()".
     * @param s1 The first string.
     * @param s2 The second string.
     * @return <code>true</code> iff. the two strings are anagrams.
     **/
    public static boolean isAnagram(String s1, String s2) {
        int[] CountS1 = countAlphabet(s1);
        int[] CountS2 = countAlphabet(s2);
        for (int i = 0; i < CountS1.length; i++) {
            if (CountS1[i] != CountS2[i]){
                return false;
            }
        }
        return true;
    }
}
