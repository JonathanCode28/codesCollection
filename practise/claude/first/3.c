#include <stdio.h>

int table(int n);

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    if (n < 1 || n > 100) {
    printf("Error: number must be between 1 and 100!\n");
    return 1;
    } else {
        table(n);
    }
    return 0;
}

int table(int n) {
    for (int i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", n, i, n * i);
    }
    return 0;
}