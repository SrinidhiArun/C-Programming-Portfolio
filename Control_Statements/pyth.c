#include <stdio.h>

int main()
{
	int x, y, z;
	printf("Enter three numbers:\n");
	scanf("%d %d %d", &x, &y, &z);
	if((x < y < z) && (x*x + y*y == z*z))
		printf("%d, %d, %d are pythagorous triads", x,y,z);
	return 0;
}
