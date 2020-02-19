//But for some values of a, b, and c, the formula does not find any valid roots. Under 
//what conditions would this formula fail? Modify the quadratic method so that it will 
//reject invalid values of a, b, or c by throwing an IllegalArgumentException. 



public class Quadratic {
	public static void main(String[] args) {
		quadratic(4,10,5);

	}
	public static void quadratic(int a, int b, int c) {
    	if (a == 0) {
        	throw new IllegalArgumentException("a can't be zero.");
    	}
    
    	double determinant = b * b - 4 * a * c;

    	if (determinant < 0) {
        	throw new IllegalArgumentException("Invalid Determinant.");
    	} else {
        
        	double minusB = (-b + Math.sqrt((b*b) - 4 * a * c)) / (2 * a);
        	double plusB = (-b - Math.sqrt((b*b) - 4 * a * c)) / (2 * a);
    
        	System.out.println("First root = " + minusB);
        	System.out.println("Second root = " + plusB);
    	}
    
	}
}
