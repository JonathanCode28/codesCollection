#include <stdio.h>

int main() {
    float average;
    int grades[5];
    int sum = 0;

    for (int i = 0; i < 5; i++) {
        printf("Enter grade %d: ", i + 1);
        scanf("%d", &grades[i]);
        sum += grades[i];
    }

    int max = grades[0];
    int min = grades[0];

    for (int i = 1; i < 5; i++) {
        if (grades[i] > max) {
            max = grades[i];
        }
        if (grades[i] < min) {
            min = grades[i];
        }
    }

    average = (float)sum / 5;

    printf("Grades: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", grades[i]);
    }
    printf("\n");

    printf("Highest: %d\n", max);
    printf("Lowest: %d\n", min);
    printf("Average: %.1f\n", average);

    return 0;
}