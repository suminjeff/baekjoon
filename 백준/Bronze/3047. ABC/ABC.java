import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] numbers = new int[3];
        for (int i = 0; i < 3; i++) {
            numbers[i] = scanner.nextInt();
        }

        scanner.nextLine();
        String order = scanner.nextLine();

        Arrays.sort(numbers);

        int A = numbers[0];
        int B = numbers[1];
        int C = numbers[2];

        for (char ch : order.toCharArray()) {
            switch (ch) {
                case 'A':
                    System.out.print(A + " ");
                    break;
                case 'B':
                    System.out.print(B + " ");
                    break;
                case 'C':
                    System.out.print(C + " ");
                    break;
            }
        }
        scanner.close();
    }
}
