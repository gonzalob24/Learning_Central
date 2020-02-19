public class MutualFund extends ShareAssets //implements Assets
{
	private double totalShares;
	
	public MutualFund(String symbol, double currentPrice) 
	{
		super(symbol, currentPrice);
		totalShares = 0.0;
	}
	//returns the market value of mutual funds
	//number of shares times the price per share
	public double getMarketValue() 
	{
		return totalShares * getCurrentPrice();
	}
	//NO longer needed
	//returns the profit on the mutual fund
	//public double getProfit() 
	//{
	//	return getMarketValue() - getTotalCost();
	//}
	//
	//records purchase of the given shares at the given price
	public void purchase(int shares, double pricePerShare)
	{
		totalShares += shares;
		addCost(shares * pricePerShare);
	}
}
