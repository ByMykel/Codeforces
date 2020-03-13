import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class CF0978B_FileName {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskB solver = new TaskB();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskB {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int n = in.nextInt();
            String s = in.next();
            int countx = 0;
            int solution = 0;
            for (int i = 0; i < n; i++) {
                if (s.charAt(i) == 'x') {
                    countx++;
                    if (countx >= 3) {
                        solution++;
                    }
                } else {
                    countx = 0;
                }
            }
            out.print(solution);
        }

    }
}

