#include <stdio.h>

int main()
{
	int a, b;
	char op;
	printf("Enter the numbers and the operator:\n");
	scanf("%d%d %c", &a, &b, &op);
	switch(op)
	{
		case '+':printf("%d + %d = %d\n", a, b, a+b);
			 break;
		case '-':printf("%d - %d = %d\n", a, b, a-b);
			 break;
		case '*':printf("%d * %d = %d\n", a, b, a*b);
			 break;
		case '/':printf("%d / %d = %d\n", a, b, a/b);
			 break;
		case '%':printf("%d %% %d = %d\n", a, b, a%b);
			 break;
		default: printf("Enter a valid operator.\n");
	}
	return 0;
}
