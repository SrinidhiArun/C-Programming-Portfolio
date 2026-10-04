#include <stdio.h>

int main()
{
	int n, sum;
	printf("Enter a number:\n");
	scanf("%d", &n);
	for(; n > 9; n = sum)
		for(sum = 0; n; n /= 10)
			sum += n % 10;
	printf("Sum of the digits is %d\n", n);
	return 0;
}

