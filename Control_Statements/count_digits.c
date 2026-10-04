#include <stdio.h>


int main()
{
	int num, digit, n, count = 0;
	printf("Enter the digit and the number:\n");
	scanf("%d%d", &digit, &num);
	while(num)
	{
		n = num % 10;
		if( digit == n )
			count++;
		num /= 10;
	}
	printf(" The number of occurrences of the digit %d in the number is %d\n", digit, count);
	return 0;
}
