public class Fiction extends Books
{
    private String genre;

    public Fiction (String genre, int ISBN, int pubDate, String author, String pubName, String language, 
                    int edition, int itemID, String itemName, String itemLocation, int numberOfCopies)
    {   
        super (ISBN, pubDate, author, pubName, language, edition, itemID, itemName, itemLocation, numberOfCopies);
        this.genre = genre;
    }

    public void setGenre(String genre)
    {
        this.genre = genre;
    }

    public String getGenre()
    {
        return genre;
    }
}