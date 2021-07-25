package UCB.UC61B0;

public class Dog {

    private static int weightInPounds;
    
    // public is not the ideal way to create fields/attributes
//    public int weightInPounds;

    public Dog(int w) {
        this.weightInPounds = w;
    }
    // instance method is invoked
    // static:
    public void makeNoise() {
        if(weightInPounds < 10) {
            System.out.println("yip");
        } else if (weightInPounds < 30) {
            System.out.println("bark");
        } else {
            System.out.println("wooof");
        }
    }
    public void bark(){
        System.out.println("Moo");
    }
}
