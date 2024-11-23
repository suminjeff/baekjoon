import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int A = 0;
        int B = 0;

        // A의 점수 입력
        for (int i = 0; i < 3; i++) {
            A += (3-i)*sc.nextInt();
        }

        // B의 점수 입력
        for (int i = 0; i < 3; i++) {
            B += (3-i)*sc.nextInt();
        }

        // 결과 출력
        if (A > B) {
            System.out.println("A");
        } else if (A < B) {
            System.out.println("B");
        } else {
            System.out.println("T");
        }

        sc.close(); // Scanner 닫기
    }
}
