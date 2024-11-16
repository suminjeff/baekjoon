import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 첫 번째 줄에서 줄의 수 입력
        int N = scanner.nextInt();
        scanner.nextLine(); // 버퍼 비우기

        // 각 줄을 입력받아 줄 번호와 함께 출력
        for (int i = 1; i <= N; i++) {
            String line = scanner.nextLine();
            System.out.println(i + ". " + line);
        }

        scanner.close();
    }
}