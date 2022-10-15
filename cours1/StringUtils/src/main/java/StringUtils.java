import java.util.Arrays;

public class StringUtils {

    /**
     * Split a string according to a delimiter
     *
     * @param str The string to split
     * @param delimiter The delimiter
     * @return An array containing the substring which fall
     *          between two consecutive occurence of the delimiter.
     *          If there is no occurence of the delimiter, it should
     *          return an array of size 1 with the string at element 0
     */
    public static String [] split(String str, char delimiter){
        /*if (!str.contains(Character.toString(delimiter))) {
            return new String[]{str};
        } else {
            return str.split(String.valueOf(delimiter));
        }

         */
        if (!str.contains(Character.toString(delimiter))) {
            return new String[]{str};
        }
        int count = 1;
        for (int x = 0; x < str.length(); x++) {
            if (str.charAt(x) == delimiter) {
                count++;
            }
        }
        String[] splitted = new String[count];
        int iter = 0;
        int begin = 0;
        for (int x = 0; x < str.length(); x++) {
            if (str.charAt(x) == delimiter) {
                splitted[iter] = str.substring(begin, x);
                begin = x + 1;
                iter++;
            }
            if (x == str.length() - 1) {
                splitted[iter] = str.substring(begin, x + 1);
            }
        }
        return splitted;
    }


    /**
     * Find the first occurence of a substring in a string
     *
     * @param str The string to look in
     * @param sub The string to look for
     * @return The index of the start of the first appearance of
     *          the substring in str or -1 if sub does not appear
     *          in str
     */
    public static int indexOf(String str, String sub){
        int lenstr = str.length();
        int lensub = sub.length();
        for (int i = 0; i <= lenstr - lensub; i++) {
            if (str.substring(i, i + lensub).equals(sub)){
                return i;
            }
        }
        return -1;
    }


    /**
     * Convert a string to lowercase
     *
     * @param str The string to convert
     * @return A new string, same as str but with every
     *          character put to lower case.
     */
    public static String toLowerCase(String str){
        //return str.toLowerCase();
        char[] s1 = str.toCharArray();
        int diff = 'a' - 'A';

        for (int i=0; i < s1.length; i++) {
            if (s1[i] >= 'A' && s1[i] <= 'Z') {
                s1[i] += diff;
            }
        }
        return String.valueOf(s1);
    }


    /**
     * Check if a string is a palyndrome
     *
     * A palyndrome is a sequence of character that is the
     * same when read from left to right and from right to
     * left.
     *
     * @param str The string to check
     * @return true if str is a palyndrome, false otherwise
     */
    public static boolean palindrome(String str){
        int len = str.length();
        for (int i = 0; i < len / 2; i++) {
            if (str.charAt(i) != str.charAt(len - 1 - i)) {
               return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int a = 300;
        byte b = (byte) a;
        System.out.println(b);
    }

}
