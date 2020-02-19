
public class Array {

	public static void main(String[] args)
	{	
		int[][] data = new int[4][7];
		
		for (int r =0; r < data.length; r++)
		{
			for (int i = 3; i < data[r].length; i++)
			{
				data[r][i] = 1;
			}
		}
	}

}
