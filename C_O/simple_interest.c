#include <stdio.h>

int main(){
	double p, r, t; // declaring the variables p ,t and r
	printf("Enter the principal, rate and number of years:"); // asking the user to enter the values of p , t and r
	scanf("%le %le %le", &p, &r, &t); // scanning the input values of p, t, r
	printf("The Simple Interest for the mentioned values of principal, rate and number of years is: %le\n", ((p * t * r) / 100)); // printing the value of S.I.
	return 0;
}
