public class Magazine extends Journal
{
    protected String topic;

    public Magazine(String topic, int edition, String pubName, int pubDate, int itemID, String itemName,
                    String itemLocation, int numberOfCopies)
    {
        super (edition, pubName, pubDate, itemID, itemName, itemLocation, numberOfCopies);
        this.topic = topic;
    }

    public void setTopic(String topic)
    {
        this.topic = topic;
    }

    public String getTopic()
    {
        return topic;
    } 

}
