// Write a for loop that produces the following output:
// 1 4 9 16 25 36 49 64 81 100 
// try to modify your code so that it does not need to use the * multiplication operator.

public class Squares {
	public static void main(String[] args) {
		System.out.print("1 ");
		int count = 1;
		for (int i = 3; i <= 19; i+=2) {
			count += i;
			System.out.print(count + " ");
		}

	}
}
