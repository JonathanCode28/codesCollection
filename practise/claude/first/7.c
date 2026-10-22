#include <stdio.h>

int main() {
    int arr[6];
    int temp;
    for (int i = 0; i < 6; i++) {
        printf("Enter number %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    printf("Original array: ");
    for (int i = 0; i < 6; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    for (int i = 0; i < 3; i++) {
        temp = arr[i];
        arr[i] = arr[5 - i];
        arr[5 - i] = temp;
    }
    printf("Reversed array: ");
    for (int i = 0; i < 6; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}