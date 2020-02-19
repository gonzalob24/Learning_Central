public class NonFiction extends Books
{
    private String topic;

    public NonFiction(String topic, int ISBN, int pubDate, String author, String pubName, 
                        String language, int edition, int itemID, String itemName, String itemLocation, 
                        int numberOfCopies )
    {
        super (ISBN, pubDate, author, pubName, language, edition, itemID, itemName, itemLocation, numberOfCopies);
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