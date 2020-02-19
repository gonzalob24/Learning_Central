public class Books extends LibraryItems
{
    protected int ISBN;
    protected int pubDate;
    protected String author;
    protected String pubName;
    protected String language;
    protected int edition;

    public Books(int ISBN, int pubDate, String author, String pubName, String language, int edition, int itemID, 
                    String itemName, String itemLocation, int numberOfCopies)
    {
        super (itemID, itemName, itemLocation, numberOfCopies);
        this.ISBN = ISBN;
        this.pubDate = pubDate;
        this.author = author;
        this.pubName = pubName;
        this.language = language;
        this.edition = edition;
    }
    public void setISBN(int ISBN)
    {
        this.ISBN = ISBN;
    }

    public int getISBN()
    {
        return ISBN;
    }
}
    
