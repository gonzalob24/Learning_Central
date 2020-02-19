// Short program demonstrating examples of using return values
// Shows using the return values from methods in the Math class
// and using return values returned from methods in this class
//
// This goes a bit further than we went in class by also writing
// a max dating age method.  It also contains Math and casting
// examples which we talked about throughout lecture.
public class Dating {
    public static void main(String[] args) 
    {
        double power = Math.pow(2, 7);
                
        System.out.println("power = " + power);
        System.out.println("root = " + Math.sqrt(121));
        System.out.println();
        
	    System.out.println("casted value of power = " + (int) power);
	    System.out.println("power is still the same = " + power);

        int age = 21;
        
        // int resultAge;
        // calcMinDatingAge(age);
        
        int resultAge = calcMinDatingAge(age);
        
        System.out.println("min dating age for " + age + ": " + resultAge);
        System.out.println("min dating age for 67: " + calcMinDatingAge(67));
        System.out.println("min dating age for 24: " + calcMinDatingAge(24));
        System.out.println("min dating age for 95: " + calcMinDatingAge(95));
        System.out.println();
        
        resultAge = calcMaxDatingAge(age);
        System.out.println("max dating age for " + age + ": " + resultAge);
    } 
    
    // returns the minimum dating age given an age based on the societal
    // convention of (age / 2) + 7
    public static int calcMinDatingAge(int age) 
    {
        int resultAge = age / 2 + 7;
        return resultAge;    //returns the value from the expression that we created 
    }   
    
    // returns the maximum dating age given an age based on the societal
    // convention of minumum dating age being (age / 2) + 7
    public static int calcMaxDatingAge(int age) 
    {
        return (age - 7) * 2;  //the expression does not need to be placed in a variable, we can 
                              //we can include it in the return statment
    }
}
