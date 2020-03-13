import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class CF0071A_WayTooLongWords {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskA solver = new TaskA();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskA {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int n = in.nextInt();
            for (int i = 0; i < n; i++) {
                String word = in.next();
                int len = word.length();
                if (len > 10) {
                    out.println(word.charAt(0) + Integer.toString(len - 2) + word.charAt(len - 1));
                } else {
                    out.println(word);
                }
            }
        }

    }
}

