package eight.oop.again;

public class Address {
    private String line1;
    private String city;
    private String zipcode;

    public Address(String line1, String city, String zipcode) {
        this.line1 = line1;
        this.city = city;
        this.zipcode = zipcode;
    }

    public String getLine1() {
        return line1;
    }

    public void setLine1(String line1) {
        this.line1 = line1;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getZipcode() {
        return zipcode;
    }

    public void setZipcode(String zipcode) {
        this.zipcode = zipcode;
    }

    @Override
    public String toString() {
        return "Address{" +
                "line1='" + line1 + '\'' +
                ", city='" + city + '\'' +
                ", zipcode='" + zipcode + '\'' +
                '}';
    }
}
