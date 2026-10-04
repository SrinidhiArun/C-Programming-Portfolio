#include <stdio.h>

int main()
{
	int i, n, flag = 1;
	printf("Enter a number:\n");
	scanf("%d", &n);
	if ( n == 0 || n == 1 )
		printf("%d is not a prime\n", n);
	else
	{
	for(i = 2; i <= n / i; i++)
	{
		if(n % i == 0)
		{
			printf("%d is not a prime number\n", n);
			flag = 0;
			break;
		}
	}
	if(flag == 1)
		printf("%d is prime\n", n);
	}
	return 0;
}

