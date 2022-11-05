import java.util.ArrayList;
import java.util.Arrays;

public class Valley{
    public static void main(String[] args) {
        int[] example = new int[]{1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1};
        int[] result = valley(example);
        System.out.println(result[0]);
        System.out.println(result[1]);
    }
    /**
     * Compute the deepest valley and highest mountain
     *
     * @paramA non-empty array of slope
     * @return An array of two element. The first is the
     *         depth of the deepest valley and the second
     *         the height of the highest mountain
     */
    public static int[] valley(int[] array) {
        int[] biggestValleyMountain = new int[]{0, 0};
        int[] slopeChange = new int[array.length];
        int iter = 1;

        slopeChange[0] = 0;
        for (int i = 1; i < array.length; i++) {
            if (array[i - 1] != array[i]) {
                slopeChange[iter] = i;
                iter++;
            }
        }
        slopeChange[iter] = array.length;

        for (int i = 0; i < iter - 1; i++) {
            int biggest = Math.min(slopeChange[i + 1] - slopeChange[i], slopeChange[i + 2] - slopeChange[i + 1]);
            if (array[slopeChange[i]] > 0) {
                biggestValleyMountain[1] = Math.max(biggestValleyMountain[1], biggest);
            } else {
                biggestValleyMountain[0] = Math.max(biggestValleyMountain[0], biggest);
            }
        }

        return biggestValleyMountain;
    }
}
