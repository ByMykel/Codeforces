import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;
 
/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class CF0231A_Team {
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
            int solution = 0;
            for (int i = 0; i < n; i++) {
                int a = in.nextInt();
                int b = in.nextInt();
                int c = in.nextInt();
                if (a + b + c > 1) {
                    solution++;
                }
            }
            out.print(solution);
        }
 
    }
}
 
