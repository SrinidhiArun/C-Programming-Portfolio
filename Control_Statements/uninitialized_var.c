#include <stdio.h>

int main()
{
	int n, rem, count = 0;
	if( n == 0 )
		printf("Number of digits in the number is '1'\n");
	else
	{
		while( n )
		{
			rem = n % 10;
			n /= 10;
			count++;
		}
		printf("Number of digits in the number is %d\n", count);
	}
		return 0;
}
