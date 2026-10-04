#include <stdio.h>

int main(){
	int n;
	printf("Enter a decimal number:\n");
	scanf("%d", &n);
	printf("The decimal number is %d\n", n); // prints the decimal value
	printf("The octal equivalent is %o\n", n); // prints the octal value
	printf("The hexadecimal equivalent is %x\n", n); // prints the hexadecimal value
	return 0;
}
