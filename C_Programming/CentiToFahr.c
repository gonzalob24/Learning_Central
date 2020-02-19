//Chapter: 3
//Problem #: 32 
//Problem Description: Convert Centigrade to Fahrenheit


#include <stdio.h> 
#define RATIO 180.0/100.00

int main(void) 
{
	//declare the values
	float fahr;
	float centi;

	printf("\n\n");
	printf("Please enter the degrees in Centigrade: ");
	scanf("%f", &centi);

	//Performs the calculation Centi to Fahr

	fahr = 32 + (centi * RATIO);

	printf("%0.2f degrees centigrade is equivalent to %0.2f Fahrenheit.\n\n", centi, fahr);

	return 0;
	
}
