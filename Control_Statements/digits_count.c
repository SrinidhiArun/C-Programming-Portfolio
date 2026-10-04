#include <stdio.h>

int main()
{
	int n, count = 0;
        printf("Enter a number:\n");
        scanf("%d", &n);      
	if( n == 0 )
		count  = 1;
	else 
	{
		n = ( n  < 0 ) ? -n : n; //makes positive
		while(n)
		{
			n /= 10;
			count++;
		}
	}	
	printf("The number of digits in the number is %d\n", count);
	return 0;
}
