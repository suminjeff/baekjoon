#include <stdio.h>

int main() {
    int a;  // 사용자로부터 입력받을 아이디를 저장할 배열 (최대 50자 + NULL 문자)
    scanf("%d", &a);  // 아이디 입력받기

    // 문자열에 "??!"를 덧붙여 출력하기
    printf("%d", a-543);

    return 0;
}
