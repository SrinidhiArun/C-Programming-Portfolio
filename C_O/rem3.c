#include <stdio.h>

int  main(){
	int n;
	printf("Enter a five-digit number:\n"); // asking the user to input a 5-digit number
	scanf("%d", &n); // scans the input value entered by the user
	printf("The value of the remainder after dividing by 3 is: %d\n", n%3); //prints the remainder after dividing the number by 3
	return 0;
}
