#include <stdio.h>

int main()
{
	int n, num, flag, a, b, c;
	printf("Enter a  3-digit number:\n");
	scanf("%d", &n);
	num = n;
	if( num >= 100 && num <= 999 )
	{
        	a = num % 10;
		num /= 10;
		b = num % 10;
		num /= 10;
		c = num % 10;
		if( a != b && a != c && b != c )
		{
			if( b == 2*a && c == 3*a )
				printf("%d is a triad number\n", n);
			else 
				flag = 0;
		}
		else
			flag = 0;
	}
	else
		flag = 0;
	if( flag == 0 )
		printf("%d is not a triad\n", n);
	return 0;

}
