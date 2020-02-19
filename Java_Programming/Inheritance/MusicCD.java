public class MusicCD extends Multimedia
{
    private String style;
    private String artist;

    public MusicCD(String style, String artist, String tracks, int playDuration, int releaseDate, int itemID, String itemName, 
                    String itemLocation, int numberOfCopies)
    {
        super (tracks, playDuration, releaseDate, itemID, itemName, itemLocation, numberOfCopies);
        this.style = style;
        this.artist = artist;
    }

    public void setStyle(String style)
    {
        this.style = style;
    }

    public String getStyle()
    {
        return style;
    }

    public void setArtist(String artist)
    {
        this.artist = artist;
    }

    public String getArtist()
    {
        return artist;
    }
}