#include <stdio.h>

int main()
{
	int a, b ,c;
	printf("Enter 3 numbers:\n");
	scanf("%d %d %d", &a, &b, &c);
	if(a > b)
	{
		if(a > c)
		{
			printf("Largest number = %d\n", a); // a is the largest number
			if(b > c)
			{
				printf("Second Largest number = %d\nSmallest number = %d\n", b, c); // b is the second largest number & c is the smallest number
			}
			else
			{ 
				printf("Second Largest number = %d\nSmallest number = %d\n", c, b); // c is the second largest number & b is the smallest number
			}
		}
		else
		{
			printf("Largest number = %d\nSecond Largest number = %d\nSmallest number = %d\n ", c, a, b); // c is the largest number, a is the second largest & b is the smallest 
		}
	}
	else
	{
		if(b > c)
		{
			printf("Largest number = %d\nSecond Largest number = %d\nSmallest number = %d\n", b, c, a); // b is the largest number, c is the second largest number & a is the smallest number
		}
		else
		{
			printf("Largest number = %d\nSecond Largest number = %d\nSmallest number = %d\n", c, b, a); // c is the largest number, b is the second largest number & a is the smallest number
		}
	}
	return 0;
}
