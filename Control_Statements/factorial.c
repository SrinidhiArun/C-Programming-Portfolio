#include <stdio.h>

int main()
{
	int  n;
        long fact = 1;
	printf("Enter a number:\t");
	scanf("%d", &n);
	if( n < 0 )
		printf("Factorial of negative numbers do not exist\n");


	while( n )
	{
		fact *= n;
		n--;
	}
	printf("The factorial of the number entered is: %ld\n", fact);
	return 0;
}
