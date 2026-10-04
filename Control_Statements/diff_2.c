#include <stdio.h>

int main()
{
	int n, i;
	printf("Enter the number:\n");
	scanf("%d", &n);
	for( i = n; i >= 2; i -= 2)
		printf("%d\t", i);
	return 0;
}
