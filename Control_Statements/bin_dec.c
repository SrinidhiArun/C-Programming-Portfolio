#include <stdio.h>

int main()
{
	int n, rem, d, j = 1, dec = 0;
	printf("Enter a number:\t");
	scanf("%d", &n);
	while( n )
	{
		rem = n % 10;
		d = rem * j;
		dec += d;
		j *= 2;
		n /= 10;
	}
	printf("The decimal equivalent is %d\n", dec);
	return 0;
}
