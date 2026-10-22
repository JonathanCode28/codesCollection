#include <stdio.h>

int power(int base, int exp);
int is_even(int n);
int absolute(int n);

int main() {
    int base, exp, power_result;

    printf("Enter base: ");
    scanf("%d", &base);
    printf("Enter exponent: ");
    scanf("%d", &exp);

    power_result = power(base, exp);

    printf("%d ^ %d = %d\n", base, exp, power_result);
    printf("Is %d even? %s\n", power_result, is_even(power_result) ? "Yes" : "No");

    printf("Absolute value of %d: %d\n", -power_result, absolute(-power_result));

    return 0;
}

int power(int base, int exp) {
    int result = 1;
    for (int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

int is_even(int n) {
    return n % 2 == 0;
}

int absolute(int n) {
    return n < 0 ? -n : n;
}