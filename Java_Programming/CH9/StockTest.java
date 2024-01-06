public class StockTest extends ShareAssetsTest{

    public StockTest(String name) {
        // need to call super of parent class to refer to behavior from superclass
        super(name);
    }

    public double getMarketValue() {
        // Need to use super only when accessing overridden methods or constructors from the superclass
        return super.getMarketValue() * 4;
    }

}
