import java.util.*;

public class RemoveRange1
{
    public static void main(String[] args)
    {
        ArrayList<Integer> list1 = new ArrayList<>(
                Arrays.asList(0, 0, 2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12, 0, 14, 0, 16));
        remRange(list1, 0, 5, 13);
        System.out.println(list1);
    }

    public static void remRange(ArrayList<Integer> numList, int value, int start_idx, int end_idx)
    {
        for (int idx = start_idx; idx < end_idx; idx++)
        {
            if (numList.get(idx) == value)
            {

                numList.remove(idx);
                start_idx--;
                end_idx--;
            }
        }
    }
}
