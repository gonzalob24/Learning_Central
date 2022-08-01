package eight.oop.again;

public class Customer {
    // the address is a class as well, this is Object Composition
    // what is the relationship between the classes
    private Address homeAddress;
    private Address workAddress;
    private String name;

    // is state mandatory when creating an object?
    // if so add it to the constructor


    public Customer(String name, Address homeAddress) {
        this.homeAddress = homeAddress;
        this.name = name;
    }

    public Address getHomeAddress() {
        return homeAddress;
    }

    public void setHomeAddress(Address homeAddress) {
        this.homeAddress = homeAddress;
    }

    public Address getWorkAddress() {
        return workAddress;
    }

    public void setWorkAddress(Address workAddress) {
        this.workAddress = workAddress;
    }

    @Override
    public String toString() {
        return "Customer{" +
                "homeAddress=" + homeAddress +
                ", workAddress=" + workAddress +
                ", name='" + name + '\'' +
                '}';
    }
}
