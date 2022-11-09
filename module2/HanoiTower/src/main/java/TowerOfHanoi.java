import java.util.Random;
import java.util.Stack;

public class TowerOfHanoi{
    public static void main(String[] args) {
        towerOfHanoiString(3, "A", "B", "C");
    }
    /**
     * Solve the Tower of Hanoi puzzle
     *
     * @param n The number of disks to move
     * @param a The tower from which we want to move the disks
     * @param b An intermediate tower
     * @param c The tower to which we want to move the disks
     */
    public static void towerOfHanoi(int n, Stack<Disk> a, Stack<Disk> b, Stack<Disk> c) {
        if (n == 1) {
            c.push(a.pop());
        } else {
            towerOfHanoi(n - 1, a, c, b);
            c.push(a.pop());
            towerOfHanoi(n - 1, b, a, c);
        }
    }
    public static void towerOfHanoiString(int n, String start, String auxiliary, String end) {
        if (n == 1) {
            System.out.println(start + " -> " + end);
        } else {
            towerOfHanoiString(n - 1, start, end, auxiliary);
            System.out.println(start + " -> " + end);
            towerOfHanoiString(n - 1, auxiliary, start, end);
        }

    }
}
