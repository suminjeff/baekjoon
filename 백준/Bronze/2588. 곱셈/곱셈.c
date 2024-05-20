#include <stdio.h>

int main() {
    int num1, num2;
    int step1, step2, step3, result;

    scanf("%d", &num1);
    scanf("%d", &num2);
    
    // 각 자릿수를 계산합니다.
    int num2_ones = num2 % 10;        // num2의 1의 자리 숫자
    int num2_tens = (num2 / 10) % 10; // num2의 10의 자리 숫자
    int num2_hundreds = num2 / 100;   // num2의 100의 자리 숫자

    // 곱셈의 각 단계별 결과를 계산합니다.
    step1 = num1 * num2_ones;
    step2 = num1 * num2_tens;
    step3 = num1 * num2_hundreds;
    result = num1 * num2;

    // 결과를 출력합니다.
    printf("%d\n", step1);
    printf("%d\n", step2);
    printf("%d\n", step3);
    printf("%d\n", result);
    
    
    return 0;
}