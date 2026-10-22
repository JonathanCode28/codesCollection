#include <stdio.h>

int calculate(int a, int b, char op);

int main() {
    int num1, num2;
    char op;
    printf("Enter two integers and operator: ");
    scanf("%d %d %c", &num1, &num2, &op);

    int result = calculate(num1, num2, op);
    printf("The result is: %d\n", result);
    return 0;
}
int calculate(int a, int b, char op) {
    switch (op) {
        case '+':
            return a + b;
        case '-':
            return a - b;
        case '*':
            return a * b;
        case '/':
            if (b == 0) {
                printf("Error: Division by zero\n");
                return 0;
            }
            return a / b;
        default:
            printf("Invalid operator\n");
            return 0;
    }
}
