public class Array2
{
    public static void main(String[] args)
    {
        int[][] a = {{3, 2, 3, 6, 7}, {4, 5, 6}}; //mannually entering an array

        int[] b = {10, 45, 67, 88, 0, 66};

        int[][] first = new int [6][4];

        System.out.println(first[4].length + " length of first");

        int[] c = new int[6];

        int counter = 0;
        
        while (counter < b.length)
        {

            System.out.print(b[counter] + "  ");
            counter++;
        }


    /*

        int x = 50;
        change(x);
        System.out.println(x);

    }

    public static void change(int val)
    {
        val = val * 2;
    */

    }
}