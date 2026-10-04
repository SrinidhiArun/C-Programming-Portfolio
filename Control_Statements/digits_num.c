#include <stdio.h>

int main()
{
	int n, rem, count = 0;
	printf("Enter a number:\t");
	scanf("%d", &n);
	do
	{
		rem = n % 10;
		count++;
		n /= 10;
	}while( n );
	printf("The number of digits in the given number is %d\n", count);
	return 0;
}
