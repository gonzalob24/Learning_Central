//Polymorphism implementation 
public class EmploayeeMain3 
{

	public static void main(String[] args) 
	{
		Employee edna = new Employee();
		Lawyer lucy = new Lawyer();
		Secretary stan = new Secretary();
		LegalSecretary leo = new LegalSecretary();
		
		Secretary steve = new LegalSecretary();
		//steve.fileLegalBriefs(); error because method is not in superclass
		steve.takeDictation("Hi");
		
		printInfo(edna);
		printInfo(lucy);
		printInfo(stan);
		printInfo(leo);
	}
	
	// Prints information about any kind of employee.
	//This method is polymorphic because the behavior will take many forms depending on
	//what type of employee is passed as the parameter.
	public static void printInfo(Employee e)
	{
		System.out.print(e.getHours() + ", ");
		System.out.printf("$%.2f, ", e.getSalary());
		System.out.print(e.getVacationDays() + ", ");
		System.out.print(e.getVacationForm() + ", ");
		//takeDictation is not defined in Employee and code will not compile.
		//System.out.println(e.takeDictation() + ", ");
		System.out.println(e); // toString representation of employee
	}

}
