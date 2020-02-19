import java.util.*;

public class StockMain 
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		
		//first stock
		System.out.print("First stock's symbol: ");
		String symbol1 = input.next();
		Stock2 stock1 = new Stock2(symbol1);
		double profit1 =makePurchases(stock1, input);
		
		//second stock
		System.out.print("Second stock's symbol: ");
		String symbol2 = input.next();
		Stock2 stock2 = new Stock2(symbol2);
		double profit2 = makePurchases(stock2, input);
		
		//reports which stock made more money
		if (profit1 > profit2)
		{
			System.out.println(symbol1 + " was more profitable than " + symbol2 + "." );

		} else if (profit2 > profit1){
			System.out.println(symbol2 + " was more profitable than " + symbol1 + "." );

		} else {
			System.out.println(symbol1 + " and " + symbol2 + "are equally profitable." );

		}
	
	}
	
	//makes purchases of stock and returns the profit
	public static double makePurchases(Stock2 currentStock, Scanner input)
	{
		System.out.print("How many purchases did you make? ");
		int numPurchases = input.nextInt();
		
		//ask about each purchase
		for (int i = 1; i <= numPurchases; i++)
		{
			
			System.out.print(i + ": How many shares and at what price per share? ");
			int numShares = input.nextInt();
			double pricePerShare = input.nextDouble();
			//ask the Stock object to record the purchase
			currentStock.purchase(numShares, pricePerShare);
		}
		//Use the Stock object to compute the profit
		System.out.print("What is today's price per share? ");
		double currentPrice = input.nextDouble();
		
		double profit = currentStock.getProfit(currentPrice);
		System.out.println("Net profit/loss: $" + profit);
		System.out.println();
		return profit;
	}
}
