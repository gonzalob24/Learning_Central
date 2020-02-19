public class LibraryItems
{
    protected int itemID;
    protected String itemName;
    protected String itemLocation;
    protected int numberOfCopies;

    public LibraryItems(int itemID, String itemName, String itemLocation, int numberOfCopies)
    {
        this.itemID = itemID; 
        this.itemName = itemName;
        this.itemLocation = itemLocation;
        this.numberOfCopies = numberOfCopies;

    }
    public void setItemID(int itemID)
    {
        this.itemID = itemID;
    }

    public int getItemID()
    {
        return itemID;
    }

    public void setItemName(String itemName)
    {
        this.itemName = itemName;
    }
    
    public String getItemName()
    {
        return itemName;
    }

    public void display()
    {
        System.out.println("The item number is " + itemID);
    }
}