#include <stdio.h>

int main()
{
	int n;
	printf("Enter a number:\t");
	scanf("%d", &n);
	while(n >= 2)
	{
		printf("%d\n", n);
		n = n-2;
	}
	return 0;
}
