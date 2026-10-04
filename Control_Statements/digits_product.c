#include <stdio.h>

int main()
{
	int n, rem, prod = 1;
	printf("Enter a number:\t");
	scanf("%d", &n);
	while(n)
	{
		rem = n %10;
		prod *= rem;
		n /= 10;
	}
	printf("The product of all the digits in the number is %d\n", prod);
	return 0;
}
