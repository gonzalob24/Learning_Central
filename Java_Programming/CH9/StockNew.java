public class StockNew extends ShareAssets //implements Assets no longer need since it extends in ShareAssests
{
	private int totalShares;
	
	//initialize new stock with no shares purchased
	public StockNew(String symbol, double currentPrice)
	{
		super(symbol, currentPrice);
		totalShares = 0;
	}
	
	//returns total shares purchased
	public int getTotalShares()
	{
		return totalShares;
	}
	
	//return market value
	//number of total shares times the share price
	public double getMarketValue()
	{
		return totalShares * getCurrentPrice();
	}
	
	//no longer needed since it is in the abstract class
	//return the profit made on this stock
	//public double getProfit() 
	//{
	//	return getMarketValue() - getTotalCost();
	//}
	//
	//records purchase of the given number of shares
	public void purchase(int shares, double pricePerShare)
	{
		totalShares += shares;
		addCost(shares * pricePerShare);
	}
	
}	
