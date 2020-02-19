import java.util.*;

public class CalendarDatesTest
{
    public static void main(String[] args)
    {
        ArrayList<CalendarDate> dates = new ArrayList<>();
        dates.add(new CalendarDate(2, 22));
        dates.add(new CalendarDate(10, 39));
        dates.add(new CalendarDate(4, 13));
        dates.add(new CalendarDate(3, 16));
        dates.add(new CalendarDate(4, 28));

        System.out.println(dates);
        System.out.println();
        Collections.reverse(dates);
        System.out.println(dates);
    }
}
