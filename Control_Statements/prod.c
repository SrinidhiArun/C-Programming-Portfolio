#include <stdio.h>

int main()
{
	int i, a, b, prod = 0;
	printf("Enter two numbers:\n");
	scanf("%d %d", &a, &b);
	for(i = 1; i <= b; i++)
		prod += a;
	printf("%d * %d = %d\n", a, b, prod);
	return 0;
}
