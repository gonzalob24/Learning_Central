//Gonzalo Betancourt
//CSCI 1320.2
//Date: 11/24/19
//Assignment # Program IV
//Program can run in Windows, Mac or Linux
//Files included: main, header files, input/output, excutable, etc..
//Purpose: The purpose of the program is to make a a few different programs
		 //working with arrays.
		 //1. Create an array of 100 random numbers in the range of 1…999, write a function for each 
		 //of the following processes. In building the array, if 3 or 7 evenly divide the random number, 
		 //store it as a negative number.

		 //a. Print the array ten values to a line. Make sure that the values are aligned in rows.

		 //b. Return a count of the number of even values

		 //c. Return the sum of all values in the array       

 		 //2. Create a two dimensional array (size 10 X 10). Fill this two dimensional array with the values 
         //from the above single dimensional array. Determine the maximum value in each row.  Display the 
         //two-dimensional array and the maximum of each row.

		 //3. Repeat number 2 above but this time instead of 10 X 10 array, prompt the user for the size of 
         //the row and column, allow user to fill in the values and display the array.(Hint: Use pointers 
	     //and dynamic memory allocation )
//Input: There is input for part 3 of this program. The user will select the size of 
		 //rows and columns. They The user will enter the value for each element
		 //of the array.
//Preconditions: The only thing we need to make sure we do is declare the size of the 
		 //array for each part except for part 3.
//Output: The out put varies by part but it includes printing arrays	
//Postconditions: None
//Algorithm: creat a random array 
		   //if an element is divisble by 3 or 7 make the element negative	
		   //store the negative value 
		   //print the array
		   //return even values
		   //return sum of the array
		   //create a 10 x 10 array
		   // fill array with previous 1D array
		   //Check each row for max value 
		   //print max value.	  
//Error: 
//Example: 
//History:

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>


void printArr(int array[], int size);
int evenElements(int array[], int size);
int arraySum(int array[], int size);
void twoD(int array[], int size);
void getArray();
int main()
{
	//cresates random numbers evrytime
	int evenTotal;
	int sumArray;
	int size = 100;
	srand(time(NULL));
	int range = 999 - 1;
	int rows = size/10;
	int cols = size/10;

	int arrayTen[rows][cols];

	int array[size];
	for (int i = 0; i < size; i++)
	{	
		int value = rand() % range + 1;
		if ( (value % 3 == 0) || (value % 7 == 0) )
		{
			array[i] = -1 * value;
		}
		else 
		{
			array[i] = value;	
		}
	}
	
	printArr(array, size);
	evenTotal = evenElements(array, size);
	printf("The total number of even values is: %d\n\n", evenTotal);

	sumArray = arraySum(array, size);
	printf("The sum of all the elements in the array is: %d\n\n", sumArray);
	
	//prints the 2d array
	twoD(array, size);
 	
 	//Method that calls the user to select the size of 
 	//rows and cols and also inputs the data for each element in the array
 	getArray();
	 

	return 0;
	

}

//function that prints the randomArray in 10 x 10 format
 void printArr(int array[], int size)
 {
 	for (int i = 0; i < size; i++)
 	{
 		if (i % 10 == 0)
 		{
 			printf("\n");
 		}
 		printf("%d\t", array[i]);
 	}

 	printf("\n\n");

 	return;

 }

 //returns the count of number of even values
 int evenElements(int array[], int size)
 {	
 	int count = 0;
 	for (int i = 0; i < size; i++)
 	{
 		if ( array[i] % 2 == 0 )
 		{
 			count++;
 		}
 	}

 	return count;
 }

 //returns the sum of all the values in the array

 int arraySum(int array[], int size)
 {
 	int sum = 0;

 	for (int i = 0; i < size; i++)
 	{
 		sum += array[i];
 	}

 	return sum;
 }
//2D array
void twoD(int array[], int size)
{
	int max = 0;
	int arrayTen[size/10][size/10];
	int count = 0;
	for (int i = 0; i < size/10; i++)
	{
		for (int j = 0; j < size/10; j++)
		{
			arrayTen[i][j] = array[count];
			count++;
		}
	}

	for (int i = 0; i < size/10; i++)
	{
		for (int j = 0; j < size/10; j++)
		{
			printf("%d\t", arrayTen[i][j]);
		}
		printf("\n");
	}
	printf("\n\n");

	for (int i = 0; i < size/10; i++)
	{
		for (int j = 0; j < size/10; j++)
		{
			if ( max < arrayTen[i][j])
			{
				max = arrayTen[i][j];
			}
		}
		printf("The max number in row %d is %d: \n", i, max);
		max = 0;
	}
	printf("\n\n");

	return;
}
//user selects the data for the array
void getArray()
{	
	int rows;
	int cols;
	int value;
	int max = 0;

	printf("Please enter the size of the rows: ");
	scanf("%d", &rows);
	printf("Please enter the size of the columns: ");
	scanf("%d", &cols);

	int array[rows][cols];

	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			printf("Enter values for the elements:");
			scanf("%d", &value);
			array[i][j] = value;
		}
	}
	printf("\n\n");

	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			printf("%d\t", array[i][j]);
		}
		printf("\n");
	}

	printf("\n\n");

	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			if (max < array[i][j])
			{
				max = array[i][j];
			}
		}

		printf("The max number in row %d is %d:\n", i, max);
		max = 0;
	}

	return;
}







