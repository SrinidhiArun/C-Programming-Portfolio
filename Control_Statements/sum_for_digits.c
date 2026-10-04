#include <stdio.h>

int main()
{
	int n, temp, rem, sum = 0;
	printf("Enter the number:\n");
	scanf("%d", &n);

	temp = (n < 0) ? -n : n;
	
	for(; temp; temp /= 10)
	{
		rem = temp % 10;
		sum += rem;
	}

	if( n == 0 )
		sum = 0;
	printf("Sum of the digits is %d\n", sum);
	return 0;
}
