//create an inheritance class using extends
public class BaseEmployee extends CommissionEmployee
{
   private double baseSalary;

   //6 argument constructor
   //for parameters include all of them from the Superclass to inherit instance variabls and methods
   //the constructor is not inherited
   

   public BaseEmployee(String firstName, String lastName, String socialSecurityNumber, double grossSales,
                     double commissionRate, double baseSalary)
   {
      //explicit call to superclass CommissionEmployee construtor
      super(firstName, lastName, socialSecurityNumber, grossSales, commissionRate);
   
      //if baseSalary is invalid throw exception
      if (baseSalary < 0.0)
      {
         throw new IllegalArgumentException("Base Salary must ne >= 0.0");
      }
   
      this.baseSalary = baseSalary;
   }

   //set base salary
   public void setBaseSalary(double baseSalary)
   {
      if (baseSalary < 0.0)
      {
         throw new IllegalArgumentException("Base Salary must be >= 0.0");
      }
   
      this.baseSalary = baseSalary;
   }

   //return base salary
   public double getBaseSalary()
   {
      return baseSalary;
   }

//calculate earnings
   @Override
   public double earnings()
   {   
      //not allowed from superclass, use super.name to invoke overridden mether in superclass
      return getBaseSalary() + super.earnings();
   }
   @Override
   //return string representation of the BaseEmployee
   public String toString()
   {
      //not allowed: attmepts to access private superclass members
      //we can change the variables in superclass to protected
      return String.format("%s %s%n%s: %.2f",
                          "base-salaried commission employee",super.toString(),
                          "base salary", getBaseSalary());
   
   }
}