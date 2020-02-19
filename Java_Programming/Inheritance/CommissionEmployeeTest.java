//import java.util.*;

public class CommissionEmployeeTest
{
    public static void main(String[] args)
    {
        
        CommissionEmployee employee = new CommissionEmployee("Sue", "Jones", "222-22-2222", 10000, .06);
        
        //get commission employee data
        System.out.println("Employee information obtained by get methods: ");
        System.out.printf("%n%s %s%n", "First name is ", employee.getFirstName());
        System.out.printf("%n%s %s%n", "Last name is ", employee.getLastName());
        System.out.printf("%n%s %s%n", "Social security numberi is ", employee.getSocialSecurityNumber());
        System.out.printf("%s %.2f%n", "Gross Sales are ", employee.getGrossSales());
        System.out.printf("%s %.2f%n", "Commission rate is ", employee.getCommissionRate());

        employee.setGrossSales(5000);
        employee.setCommissionRate(0.1);

        //runtime error and stops working this this printf stmt
        System.out.printf("%n%s:%n%n%s%n", "Update employee information obtained by toString", employee);
        
        //System.out.println(employee);
    }
}