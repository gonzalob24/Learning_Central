public class Multimedia extends LibraryItems
{
    protected String tracks;
    protected int playDuration;
    protected int releaseDate;

    public Multimedia(String tracks, int playDuration, int releaseDate, int itemID, String itemName, 
                        String itemLocation, int numberOfCopies)
    {
        super(itemID, itemName, itemLocation, numberOfCopies);
        this.tracks = tracks;
        this.playDuration = playDuration;
        this.releaseDate = releaseDate;
    }

    public void setTracks(String tracks)
    {
        this.tracks = tracks;
    }

    public String getTracks()
    {
        return tracks;
    }
}