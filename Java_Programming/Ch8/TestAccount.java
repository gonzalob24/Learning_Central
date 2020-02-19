public class TestAccount
{
   public static void main(String[] args)
   {
      SavingsAccount savingsAcc = new SavingsAccount("S1001", 5000);
      savingsAcc.display();
      savingsAcc.withdraw(2000);
      savingsAcc.display();
   
   }
}