public class Stock2 {
	private String symbol;
	private int totalShares;
	private double totalCost;

	// initialize new stock with no shares purchased
	public Stock2(String symbol) {
		if (symbol == null) {
			throw new NullPointerException();
		}

		this.symbol = symbol;
		totalShares = 0;
		totalCost = 0.0;
	}

	// get profit or loss
	public double getProfit(double currentPrice) {
		if (currentPrice < 0.0) {
			throw new IllegalArgumentException();
		}

		double marketValue = totalShares * currentPrice;
		return marketValue - totalCost;
	}

	// records purchase of given shares
	public void purchase(int shares, double pricePerShare) {
		if (shares < 0 || pricePerShare < 0.0) {
			throw new IllegalArgumentException();
		}

		totalShares += shares;
		totalCost += shares * pricePerShare;

	}
}
