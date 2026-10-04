#include <stdio.h>

int main()
{
	int n, sum = 0;
	do
	{
		printf("Enter a number (0 to stop):\n");
		scanf("%d", &n);
		sum += n;
	}while(n);
	printf("Sum of entered numbers is %d\n", sum);
	return 0;
}
