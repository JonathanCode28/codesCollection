#include <stdio.h>

int main() {
    int comp_num, user_num, attempts;
    comp_num = 42;
    attempts = 0;
    
    do {
        printf("Guess the number: ");
        scanf("%d", &user_num);
        attempts++;  // ספור כל ניסיון

        if (user_num < comp_num) {
            printf("Too low!\n");
        } else if (user_num > comp_num) {
            printf("Too high!\n");
        }
    } while (user_num != comp_num);

    printf("You guessed the number in %d attempt(s).\n", attempts);
    return 0;
}