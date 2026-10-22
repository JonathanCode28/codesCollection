#include <stdio.h>

int add(int a, int b);
char get_grade(int score);
char* get_day(int n);
void print_line(int n);

int main() {
    int a, b, score, day, n;
    printf("Enter two numbers to add: ");
    scanf("%d %d", &a, &b);
    printf("Enter a score to get the grade: ");
    scanf("%d", &score);
    printf("Enter a day number (1-7): ");
    scanf("%d", &day);
    printf("Enter the number of dashes for the line: ");
    scanf("%d", &n);

    printf("Sum: %d\n", add(a, b));
    printf("Grade: %c\n", get_grade(score));
    printf("Day: %s\n", get_day(day));
    print_line(n);
    return 0;
}

int add(int a, int b) {
    return a + b;
}

char get_grade(int score) {
    if (score >= 90) return 'A';
    else if (score >= 80) return 'B';
    else if (score >= 70) return 'C';
    else if (score >= 60) return 'D';
    else return 'F';
}

char* get_day(int n) {
    switch (n) {
        case 1: return "Monday";
        case 2: return "Tuesday";
        case 3: return "Wednesday";
        case 4: return "Thursday";
        case 5: return "Friday";
        case 6: return "Saturday";
        case 7: return "Sunday";
        default: return "Invalid day";
    }
}

void print_line(int n) {
    for (int i = 0; i < n; i++) {
        printf("-");
    }
    printf("\n");
}