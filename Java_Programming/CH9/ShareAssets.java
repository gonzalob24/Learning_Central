public abstract class ShareAssets implements Assets
{
	private String symbol;
	private double totalCost;
	private double currentPrice;
	public ShareAssets(String symbol, double currentPrice) 
	{
		this.symbol = symbol;
		this.currentPrice = currentPrice;
		this.totalCost = 0.0;
	}
	
	//returns the current market value of this asset
	public abstract double getMarketValue();
	
	//sets the current share price of this asset
	public void setCurrentPrice(double currentPrice)
	{
		this.currentPrice = currentPrice;	
	}
	
	//returns price per share of this asset
	public double getCurrentPrice()
	{
		return currentPrice;
	}
	
	//adds cost of the given amount to this asset
	public void addCost(double cost)
	{
		totalCost += cost;
	}
	
	//returns total cost for all shares
	public double getTotalCost()
	{
		return totalCost;
	}
	
	//return the profit made on this stock
	public double getProfit() 
	{
		return getMarketValue() - totalCost;
	}
}
