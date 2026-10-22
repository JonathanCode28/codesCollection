#include <stdio.h>

int main() {
    int numbers[5];
    int *start_ptr = numbers; // first element
    int *end_ptr = numbers + 4; // last element

    printf("Enter 5 integers:\n");
    for (int i = 0; i < 5; i++) {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &numbers[i]);
    }

    printf("First element: %d\n", *start_ptr);
    printf("Last element: %d\n", *end_ptr);

    printf("First element address: %p\n", (void*)start_ptr);
    printf("Last element address: %p\n", (void*)end_ptr);
    return 0;
}