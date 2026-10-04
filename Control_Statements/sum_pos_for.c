#include <stdio.h>

int main()
{
        int n, count, sum = 0;
        printf("Enter 10 positive numbers:\n");
        for(count = 1; count <= 10;)
	{
		printf("Enter number %d:\n", count);
		if( (scanf("%d", &n)) != 1 )
		{
			printf("Invalid input, integers only.\n");
			while( getchar() != '\n' ); //clear buff
			continue;
		}
		
		if( n < 0 )
		{
			printf("Enter only positive integers.\n");
			continue;
		}
		sum += n;
		count++;
	}
	printf("Final Sum = %d\n", sum);
        return 0;
}

