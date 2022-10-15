public class CommonElements {
    public static void main(String[] args){
        int[][] tab1 = new int[][]{{0,1,2,3},{2,4,5,5},{1,5,4,4},{0,0,0,0}};
        int[][] tab2 = new int[][]{{0,1,2,3,4},{2,3,5,5,4},{1,1,5,5,5}};
        //int count = count(tab1,tab2);
        System.out.println(tab2.length);
    }
    /**
     *
     * @param tab1 is a non null array
     * @param tab2 is a non null array
     * @return the number of elements that are the same at the same index
     *         more exactly the size of set {i such that tab1[i] == tab2[i]}
     *         for instance count([1,3,5,5],[1,2,5,5,6]) = 3
     */
    public static int count(int [] tab1, int [] tab2) {
        int len = Math.min(tab1.length, tab2.length);
        int counter = 0;
        for (int i = 0; i < len; i++) {
            if (tab1[i] == tab2[i]){
                counter++;
            }
        }
        return counter;
    }


    /**
     *
     * @param tab1 is a non null 2D array
     * @param tab2 is a non null 2D array
     * @return the number of elements that are the same at the same index
     *         more exactly the size of set {(i,j) such that tab1[i][j] == tab2[i][j]}
     */
    public static int count(int [][] tab1, int [][] tab2) {
        int len = Math.min(tab1[0].length, tab2[0].length);
        int height = Math.min(tab1.length, tab2.length);
        int counter = 0;
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < len; j++) {
                if (tab1[i][j] == tab2[i][j]){
                    counter++;
                }
            }
        }
        return counter;
    }
}
