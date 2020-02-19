public class Journal extends LibraryItems
{
    protected int edition;
    protected String pubName;
    protected int pubDate;

    public Journal(int edition, String pubName, int pubDate, int itemID, String itemName, String itemLocation, int numberOfCopies)
    {
        super(itemID, itemName, itemLocation, numberOfCopies);
        this.edition = edition;
        this.pubName = pubName;
        this.pubDate = pubDate;
    }

    public void setEdition(int edition)
    {
        this.edition = edition;
    }
    public int getEdition()
    {
        return edition;
    }

}