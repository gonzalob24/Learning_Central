public class DogMain {
    public static void main(String[] args) {
        int[] nums = new int[5];
        int[] array = new int[]{1,2,3,4,5};
//        Dog d1 = new Dog(28);
//        d1.weightInPounds = 28;
//        Dog.makeNoise();

//        d1.makeNoise();
        // Dog instance can only call static methods
        for (int i = 0; i <= nums.length; i++) {
            Dog d = new Dog(i*9);
            d.makeNoise();
            d.bark();
        }
    }
}
