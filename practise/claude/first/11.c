#include <stdio.h>

char* describe_temp(float temp);
void print_weather(float temp);

int main() {
    float temp;
    printf("Enter the temperature in Celsius: ");
    scanf("%f", &temp);
    print_weather(temp);
    return 0;
}

char* describe_temp(float temp) {
    if (temp < 0) {
        return "Freezing";
    } else if (temp < 15) {
        return "Cold";
    } else if (temp >= 15 && temp < 25) {
        return "Pleasant";
    } else if (temp >= 25 && temp < 35) {
        return "Hot";
    } else {
        return "Very Hot";
    }
}

void print_weather(float temp) {
    char* description = describe_temp(temp);
    printf("Temperature: %.1f in C -- %s\n", temp, description);
}