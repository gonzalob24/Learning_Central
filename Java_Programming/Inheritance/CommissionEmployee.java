//import java.util.*;

public class CommissionEmployee //extends Object
{
    private final String firstName;
    private final String lastName;
    private final String socialSecurityNumber;
    private double grossSales; //weekly sales
    private double commissionRate; //commission percentage

    //five argument constructor set to default values
    public CommissionEmployee(String firstName, String lastName, String socialSecurityNumber, double grossSales,
                                double commissionRate)
    {
        //implicit call to Object's defalut constructor ocurs here 
        //constructors are not inherited

        //if grossSales is invalid throw exception
        if (grossSales < 0.0)
        {
            throw new IllegalArgumentException("Gross Sales must be >= 0.0");
        }

        //if commission rate is invaldd
        if (commissionRate <= 0.0 || commissionRate >= 1.0)
        {
            throw new IllegalArgumentException("Commission Rate must be > 0.0 abd < 1.0");
        }

        this.firstName = firstName;
        this.lastName = lastName;
        this.socialSecurityNumber = socialSecurityNumber;
        this.grossSales = grossSales;
        this.commissionRate = commissionRate;
    }

    //return first name
    public String getFirstName()
    {
        return firstName;
    }

    //return last name
    public String getLastName()
    {
        return lastName;
    }

    //return social security number
    public String getSocialSecurityNumber()
    {
        return socialSecurityNumber;
    }

    //set gross sales amount
    public void setGrossSales(double grossSales)
    {
        //check if gross sales is less than 0.0
        if (grossSales < 0.0)
        {
            throw new IllegalArgumentException("Gross Sales must be >= 0.0");
        }

        this.grossSales = grossSales;
    }

    //return gross sales amount
    public double getGrossSales()
    {
        return grossSales;
    }

    //set commission rate
    public void setCommissionRate(double commissionRate)
    {
        if (commissionRate <= 0.0 || commissionRate >= 1.0)
        {
            throw new IllegalArgumentException("Commission rate must be > 0.0 and < 1.0");
        }
        this.commissionRate = commissionRate;
    }

    //return commission rate
    public double getCommissionRate()
    {
        return commissionRate;
    }

    //calculate earnings
    public double earnings()
    {
        return getCommissionRate() * getGrossSales();
    }
    
    
    //return String representation of commissionEmployee object
    @Override //indicates that this method overrides a superclass method
    public String toString()
    {
        return String.format("%s: %s %s%n%s: %s%n%s: %.2f%n%s: %.2f", 
                            "commission employee", getFirstName(), getLastName(),
                            "social security number", getSocialSecurityNumber(),
                            "gross sales", getGrossSales(),
                            "commission rate", getCommissionRate());
    }
}