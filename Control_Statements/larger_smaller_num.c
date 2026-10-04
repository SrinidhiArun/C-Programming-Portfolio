#include <stdio.h>

int main(){
	int a, b;
	printf("Enter the first number:\n");
	scanf("%d", &a);
	printf("Enter the second number:\n");
	scanf("%d", &b);
	if( a > b )
		printf("Larger number = %d, Smaller number = %d\n", a, b);
	else
		printf("Larger number = %d, Smaller number = %d\n", b, a);
	return 0;
}
