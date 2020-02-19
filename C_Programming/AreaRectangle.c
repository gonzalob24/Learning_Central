//Gonzalo Betancourt
//CSCI 1320.2
//09/07/2018
//Assignment #: 1
//Program can run in Windows, Mac or Linux
//Files included: main, header files: stdio.h
//Purpose: The programs main goal is to calculate the area of the rectangle when
	//the user inputs a length and a width
//Input: I will use a length and a width for my rectangle, the values can't be negative
//Preconditions: The data can't be negative
//Output: Lengths times width will give me the indicated area
//Postconditions: The calculated area by the program
//Algorithm: The program will multiply the length and width to calculate the area 
//Errors: (optional)
//Example: Input:
	// Please enter a nonnegative value for the lenfth of the rectangle: 
	// Please enter a nonnegative value for the width of the rectangle: 
	//      Output
	// The area of the rectanle with:
	// 	length: 
	// 	width: 
	// is:	 
//History: (optional)


#include <stdio.h>

int main(void) 
{
	float length;
	float width;
	float area;

	//prompt the user to enter the length of the rectangle
	printf("Please enter a nonnegative value for the length of the rectangle: ");
	scanf("%f", &length);
	printf("Please enter a nonnegative value for the width of the rectangle: ");
	scanf("%f", &width);

	area = length * width;

	printf("The area of the rectangle with:");
	printf("\n\tlength:%0.2f", length);
	printf("\n\twidth :%0.2f", width);
	printf("\nis\t      :%0.2f squared units\n", area);


	return 0;
	
}
