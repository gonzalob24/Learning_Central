public class Cash implements Assets
{
	private double amount;
	
	
	//Cash constructor
	public Cash(double amount) 
	{
		this.amount = amount;
	}

	//returns the market value of cash which is going to be the amount
	public double getMarketValue() 
	{
		return amount;
	}

	//cash is fixed so profit is set to 0.0
	public double getProfit() 
	{
		return 0.0;
	}
	
	//sets amount of cash invested
	public void setAmount(double amount)
	{
		this.amount = amount;
	}
	
}
