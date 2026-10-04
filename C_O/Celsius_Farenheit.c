#include <stdio.h>

int main(){
	int c;
	printf("Enter the value in Celsius:");
	scanf("%d", &c);
	printf("The value in Farenheit is: %d\n", (c * (9/5)) + 32);
return 0;
}
