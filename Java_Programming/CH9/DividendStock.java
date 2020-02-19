public class DividendStock extends StockNew
{	
	private double dividends;

	public DividendStock(String symbol, double currentPrice) 
	{
		super(symbol, currentPrice);
		dividends = 0.0;
	}
	
	//returns market value for dividend
	//normal stock market value plus dividends
	public double getMarketValue()
	{
		return super.getMarketValue() + dividends;
	}
	
	//records a dividend of the given amount per share
	public void payDividend(double amountPerShare)
	{
		dividends += amountPerShare * getTotalShares();
	}
}
