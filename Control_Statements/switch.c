#include <stdio.h>

int main()
{
	int n;
	printf("Enter your choice:\n");
	scanf("%d", &n);
	switch( n )
	{
		case 1:
			printf("First\n");
		case 2:
			printf("Second\n");
		case 3:
			printf("Third\n");
		default:
			printf("Wrong choice\n");
	}
	return 0;
}
