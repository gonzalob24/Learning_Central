public class SavingsAccount implements AccountIntf
{
    protected double balance;
    protected String accountNum;

    public SavingsAccount(String accountNum, double amount)
    {
        this.accountNum = accountNum;
        this.balance = amount;
    }
    //implements the menthof of interface
    public void withdraw(double amount)
    {
        if(amount <= balance)
        {
            balance -= amount;
        }else {
            System.out.println("Not enough money in your account.");
        }
    }

    //implements the method of interface
    public void deposit(double amount)
    {
        if( amount > 0 )
        {
            balance += amount;
        }else {
            System.out.println("Amount cannot be negative.");
        }
    }
    //Using the constant of interface
    public double calculateInterest()
    {
        return balance * interestRate / 100;
    }
    //
    public String toSrtring()
    {
        return "Account Num: " + accountNum + "\nBalance: " + balance;
    }

    public void display()
    {
        System.out.println(toSrtring());
    } 
}//end of class SavingsAccount