
public class Search {

    /**
     *
     * @param tab: a sorted array full of int
     *        elem: int, the element we have to find
     * @return int: the index at which the element can be found or -1 if the element was not found
     *
     */
    public static int search(int[] tab, int elem){
        int low = 0;
        int high = tab.length;
        int mid = (low+high)/2;
        while (high-low != 1) {
            if (elem == tab[mid]) {
                return mid;
            } else if (elem > tab[mid]) {
                low = mid;
                mid = (low + high) / 2;
            } else {
                high = mid;
                mid = (low + high) / 2;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] testarray = new int[]{1,2,3,7,9,10,15,66,99};
        int toFind = 11;
        System.out.println(search(testarray, toFind));
    }
}
