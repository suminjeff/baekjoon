import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String s = sc.next();
        sc.close();

        int two = 0;
        int e = 0;

        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '2') {
                two++;
            } else {
                e++;
            }
        }

        if (two > e) System.out.println(2);
        else if (two < e) System.out.println("e");
        else System.out.println("yee");


    }
}