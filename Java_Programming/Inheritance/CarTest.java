public class CarTest
{
    public static void main(String[] args)
    {
        MonsterTruck mt1 = new MonsterTruck();
        Truck t1 = new Truck();

        mt1.m1();
        mt1.m2();
        System.out.println(mt1.toString());
        System.out.println("\nTruck");
        t1.m1();
        t1.m2();
        System.out.println(t1.toString());
    }
}
