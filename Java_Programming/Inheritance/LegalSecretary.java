
public class LegalSecretary extends Secretary 
{
	public void fileLegalBriefs()
	{
		System.out.println("I could fill all day!");
	}
	
	//overrides getSalary from Employee superclass
	public double getSalary()
	{
		return  super.getSalary() + 5000.0;
	}
}
