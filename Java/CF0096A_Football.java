import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;
 
/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class CF0096A_Football {
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
            String s = in.next();
            if (s.contains("1111111") || s.contains("0000000")) {
                out.print("YES");
            } else {
                out.print("NO");
            }
        }
 
    }
}
 
