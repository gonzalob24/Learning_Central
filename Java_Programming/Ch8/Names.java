
public class Names
{
	private String firstName;
	private String lastName;
	private char middleInitial;

	public Names(String firstName, String lastName, char middleInitial)
	{
		this.firstName = firstName;
		this.lastName = lastName;
		this.middleInitial = middleInitial;
	}

	public String getFirstName()
	{
		return firstName;
	}

	public char getMiddleName()
	{
		return middleInitial;
	}

	public String getLastName()
	{
		return lastName;
	}

	public void setFirstName(String first)
	{
		this.firstName = first;
	}

	public void setMiddleInitial(char middle)
	{
		this.middleInitial = middle;
	}

	public void setLastName(String last)
	{
		this.lastName = last;
	}

	public String getNormalOrder()
	{
		return firstName + " " + middleInitial + ". " + lastName;
	}

	public String getReverseOrder()
	{
		return lastName + " " + firstName + " " + middleInitial + ".";
	}

	@Override
	public String toString()
	{
		return firstName + " " + middleInitial + ". " + lastName;
	}
}
