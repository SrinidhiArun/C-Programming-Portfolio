#include <stdio.h>

int main()
{
	int n, rem, sum = 0;
	printf("Enter a number:\t");
	scanf("%d", &n);
        while( n )
	{
	rem = n % 10;
	sum += rem;
	n /= 10;
	}
	printf("The sum of the digits in the number is %d\n", sum);
	return 0;
}
