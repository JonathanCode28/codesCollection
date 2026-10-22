#include <stdio.h>

int grade(int score);

int main() {
    int score;
    printf("Enter your score: ");
    scanf("%d", &score);
    if (score < 0 || score > 100) {
        printf("Invalid score. Please enter a score between 0 and 100.\n");
        return 0;
    }
    int result = grade(score);
    printf("Your grade is: %c\n", result);
    return 0;
}

int grade(int score) {
        switch (score / 10) {
            case 10:
            case 9:
                return 'A';
            case 8:
                return 'B';
            case 7:
                return 'C';
            case 6:
                return 'D';
            default:
                return 'F';
        }
    }
}