#include <stdio.h>

int main() {
    int A, B, C;
    scanf("%d %d", &A, &B); // 현재 시각 입력
    scanf("%d", &C); // 요리 시간 입력

    // 현재 시각을 분 단위로 환산
    int total_minutes = A * 60 + B + C;

    // 종료 시각을 시와 분으로 환산
    int end_hour = (total_minutes / 60) % 24;
    int end_minute = total_minutes % 60;

    printf("%d %d\n", end_hour, end_minute);

    return 0;
}
