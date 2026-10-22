#include <stdio.h>

int countVowels(char str[]);

int main() {
    char str[100];
    printf("Enter a string: ");
    scanf(" %[^\n]", str);
    printf("Number of vowels: %d\n", countVowels(str));
    return 0;
}

int countVowels(char str[]) {
    int count = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        char c = str[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            count++;
        }
    }
    return count;
}