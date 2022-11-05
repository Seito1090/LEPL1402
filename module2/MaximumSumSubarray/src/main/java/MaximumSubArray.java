public class MaximumSubArray {


    /**
     * Find the contiguous subarray with the maximal sum
     *
     * @param a a non-empty array
     * @return A triplet (sum, start, end) with sum the sum of the subarray and `start` and `end` the
     *         start and end of the subarray
     *
     * For example for the array [-2,1,-3,4,-1,2,1,-5,4] your method should return [6, 3, 6]
     */
    public static int[] maxSubArray(int[] a){
        // TODO: students
        int[] result = new int[]{a[0], 0, 0};
        for (int i = 0; i < a.length; i++) {
            for (int j = i; j < a.length; j++) {
                int sum = sumSubArray(a, i, j);
                if (sum > result[0]) {
                    result[0] = sum;
                    result[1] = i;
                    result[2] = j;
                }
            }
        }
        return result;
    }
    public static int sumSubArray(int[] a, int start, int end){
        int sum = 0;
        for (int i = start; i <= end; i++) {
            sum += a[i];
        }
        return sum;
    }
    public static int[] maxSubArrayOptimized(int[] a){
        int max = a[0];
        int meh = 0;
        int from = 0;
        int to = 0;
        int s = 0;
        for (int i = 0; i < a.length; i++){
            meh += a[i];
            if (max < meh){
                max = meh;
                from = s;
                to = i;
            }
            if (meh < 0){
                meh = 0;
                s = i + 1;
            }
        }
        return new int[]{max, from, to};
    }

}

