public class DVD extends Multimedia
{
    private String genre;
    private String director;

    public DVD(String genre,String director, String tracks, int playDuration, int releaseDate, int itemID, 
                String itemName, String itemLocation, int numberOfCopies)
    {
        super (tracks, playDuration, releaseDate, itemID, itemName, itemLocation, numberOfCopies);
        this.genre = genre;
        this.director = director;
    }

    public void setGenre(String genre)
    {
        this.genre = genre;
    }
    public String getGenre()
    {
        return genre;
    }

    public void setDirector(String director)
    {
        this.director = director;
    }

    public String getDirector()
    {
        return director;
    }
}