#include <stdio.h>

void print_fibonacci(int count)
{
	int first = 0;
	int second = 1;

	for (int i = 0; i < count; i++)
	{
		printf("%d ", first);

		int next = first + second;
		first = second;
		second = next;
	}
}

int main(void)
{
	int count;

	printf("Enter the number of Fibonacci terms: ");
	scanf("%d", &count);

	if (count <= 0)
	{
		printf("Please enter a non-negative number.\n");
		return 1;
	}

	print_fibonacci(count);
	printf("\n");

	return 0;
}