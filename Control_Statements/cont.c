#include <stdio.h>

int main()
{
	int n;
	for( n = 1; n <= 5; n++ )
	{
		if( n == 3 )
		{
			printf("I understand the use of continue:\n");
			continue;
		}
	printf("Number = %d\n", n);
	}
	printf("Out of the loop");
}
