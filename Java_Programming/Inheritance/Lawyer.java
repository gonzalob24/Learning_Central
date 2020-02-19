public class Lawyer extends Employee 
{
	
	public void sue()
	{
		System.out.println("I'll see you in court!");
	}
	//overrides from superclass Employee
	public int getVacattionDays()
	{
		return 15;
	}
	//overrides from superclass Employee
	public String getVacationFrom()
	{
		return "pink";
	}
}
