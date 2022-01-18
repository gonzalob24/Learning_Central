public class SavingsAccountExtended extends SavingsAccount {

    public SavingsAccountExtended(String accountNum, double amount) {
        super(accountNum, amount);
    }

    @Override
    public void withdraw(double amount) {
        super.withdraw(amount);
    }

    @Override
    public void deposit(double amount) {
        super.deposit(amount);
    }

    @Override
    public double calculateInterest() {
        return super.calculateInterest();
    }

    @Override
    public String toSrtring() {
        return super.toSrtring();
    }

    @Override
    public void display() {
        super.display();
    }
}
