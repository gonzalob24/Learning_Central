//Gonzalo Betancourt
//CSCI 1320.2
//Date: 10/08/2018
//Assignment: Program II
//Program can run in Windows, Mac or Linux
//Files included: main, header files, input/output, excutable, Function
//Purpose: The program will calculate bank charges from ABC Bank.
	//The customer in this bank can have an account as a checking or
	//money-market type
//Input: Customer will select the type of account he/she owns and
	//enter the number of checks written. 
//Preconditions: Customer must select a type of account and 
	//input postive numbers, no negative numbers allowed.
	//Input validation to make sure the numbers are not negative
  //For this program we can only validate input once since we can't use a
  //for loop or while loop.
//Output: Display the bank's fees for the month
//Postconditions: The program will calculate the bank's charges and 
	//all checks have the same charge.
//Algorithm: The fees will be determined based on the type of account and number of checks  
	//written. 
	//$15 per month for Checking account and $10 per month for Money-Market accounts 
	//Plus the following fees for the checks:
	//$0.10 < 20 written checks
	//$0.08 20 through 39 Written checks
	//$0.06 40 through 59 Written checks 
	//$0.04 >= to 60 written checks
//Error: If the user inputs a negative number the program will not proceed
	//until the user enters a valid number. The program will let the customer
	//know when he/she inputs an incorrect value.
//Example: Following is a test data example for Money-Market to determine the fees
	// Number of checks   Total Fees
	//			15				    $11.50
	//			25				    $12.00
	//			45				    $12.70
	//			75				    $13.00

#include <stdio.h>

void getData(int* accountType, int* totalChecks);
float bankCharges(int totalChecks, int accountType);
int main(void) 
{
	int accountType;
	int totalChecks;
	float fees;

	getData(&accountType, &totalChecks);

	fees = bankCharges(totalChecks, accountType);
	
	printf("Number of Checks   Total Fees\n");
	printf("       %d          $%.2f\n", totalChecks, fees);
	return 0;
	
} //main

//function that gets data from the user such as accoun type and total checks written
void getData(int* accountType, int* totalChecks)
{
	printf("Plese selct the type of account you have:\n");
	printf("1: Checking account\n");
	printf("2: Money-Market account\n");
	scanf("%d", accountType);

	//If statement checks once to validate input
	if ( !( (*accountType == 1) || (*accountType == 2) ) ) 
	{
		printf("You have entered an incorrect value.\n");
		printf("Plese selct the type of account you have:\n");
	  printf("1: Checking account\n");
	  printf("2: Money-Market account\n");
	  scanf("%d", accountType);

	} // do nothing and continue with the program
	
	printf("Please type in the total number of checks written for the selected account:");
	scanf("%d", totalChecks);

	//if statement checks once to validate input
	if (*totalChecks < 0)
	{
		printf("You have entered an incorrect value.\n");
		printf("Please type the total number of checks written: ");
		scanf("%d", totalChecks);
	} //do nothing


	return;
} //getData

//function that calcualtes the total fees charged
float bankCharges(int totalChecks, int accountType)
{	
	float feeAcc;  //fee for the type of account
	float checkFees; //fee for the checks

	if (accountType == 1)
	{
		feeAcc = 15;
	}else {
		feeAcc = 10;
	}

	switch (totalChecks / 10)
	{
		case 0:
		case 1: checkFees = 0.10;
	           break;
		case 2:
		case 3: checkFees = 0.08;
				  break;
		case 4:
		case 5: checkFees = 0.06;
			     break;
	  default: checkFees = 0.04;

	}

	return feeAcc + totalChecks * checkFees;

} //bankCharges
