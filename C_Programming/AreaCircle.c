//Gonzalo Betancourt
//CSCI 1320-2
//09/17/2018
//Assignment #: Program 1
//Program can run in Windows, Mac or Linux
//Files included: main, header files: stdio.h
//Purpose: The programs main goal is to calculate the area of the circle, 
	//Diameter, and the circumference when the user inputs the radius
//Input: I will use the radius of the circle.
//Preconditions: The data can't be negative
//Output: Area, diameter, circumference.
//Postconditions: The calculated area by the program, diameter, and radius
//Algorithm: The program will use the formulas: Diameter = 2 * radius
			  //Circumference = 2 * PI * radius
			  //Area = PI * radius * radius
			  //Pseudo code:
			  //Begin
			  //defin PI = 3.14159	
			  //float area, circumference, radius, diameter
			  //Ask user for input
			  //calculate circumference, area, diameter
			  //print the results
			  //end  
//Errors: (optional)
//Example: Input:
	// Please enter the value of the radius
	//      Output
	// Radius is:
	// Circumference is: 
	// Area is: 	 
//History: (optional)


#include <stdio.h>
#define PI 3.14159  //Global constant

int main(void)
{
	// Local Declarations
	float circumference;
	float area;
	float radius;
	float diameter;

	// Statementes
	printf("\nPlease enter the value of the radius: ");
	scanf("%f", &radius);

	//Calculates the circumference
	circumference = 2 * PI * radius;

	// Calculates the area
	area = PI * radius * radius;

	//Calculates the Diameter
	diameter = 2 * radius;

	//Prints the Radius, Circumference and the area
	printf("\nDiameter is :       %0.2f", diameter);
	printf("\nCircumference is :  %0.2f", circumference);
	printf("\nArea is :           %0.2f\n\n", area);


	return 0;
}


