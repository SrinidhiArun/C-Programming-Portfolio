#include <stdio.h>

int main()
{
	int count = 1, n, sum = 0;
	float avg;
	printf("Enter 10 positive numbers:\n");
	while(count <= 10)
	{
		printf("Enter number %d:\n", count);
		scanf("%d", &n);
		if( n < 0 )
		{
			printf("Enter only positive numbers:\n");
			continue;
		}
	sum += n;
	printf("Sum = %d\n", sum);
	count++;
	}
	return 0;
}
