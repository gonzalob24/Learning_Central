
public class EmployeeMain 
{
	public static void main(String[] args)
	{
		System.out.print("Employee: ");
		Employee edna = new Employee(); 
		System.out.print(edna.getHours() + ", ");
		System.out.printf("$%.2f, ", edna.getSalary());
		System.out.print(edna.getVacationDays() + ", ");
		System.out.println(edna.getVacationForm());
		
		System.out.print("Secretary: ");
		Secretary stan = new Secretary();
		System.out.print(stan.getHours() + ", ");
		System.out.printf("$%.2f, ", stan.getSalary());
		System.out.print(stan.getVacationDays() + ", ");
		System.out.println(stan.getVacationForm());
		stan.takeDictation("hello");
	}
}
