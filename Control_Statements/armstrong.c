#include <stdio.h>

int main()
{
	int n, rem, num, cube, sum = 0;
	for (num = 100; num <= 999; num++)
	{
		n = num;
		sum = 0;
		while(n)
		{
			rem = n % 10;
			n /= 10;
			cube = rem * rem * rem;
			sum += cube;
		}
	if( num == sum )
		printf("%d\t", num);
	}
	return 0;
}
