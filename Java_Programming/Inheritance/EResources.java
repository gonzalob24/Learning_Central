public class EResources extends Journal
{
    private int LastUpdated;
    private String topic;
    private String type;

    public EResources(int LastUpdated, String topic, String type, int edition, String pubName, int pubDate, 
                        int itemID, String itemName, String itemLocation, int numberOfCopies)
    {
        super(edition, pubName, pubDate, itemID, itemName, itemLocation, numberOfCopies);
        this.LastUpdated = LastUpdated;
        this.topic = topic;
        this.type = type;
    }

    public void setLastUpdated(int LastUpdated)
    {
        this.LastUpdated = LastUpdated;
    }

    public int getLastUpdated()
    {
        return LastUpdated;
    } 
}