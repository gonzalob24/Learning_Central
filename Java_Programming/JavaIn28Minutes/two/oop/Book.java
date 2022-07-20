package two.oop;

public class Book {
    private int noOfCopies;

    public Book() {
        // default constructor does not get called when I create a constructor
        // when I don't create a constructor the default is called by the java compiler
    }

    public Book(int noOfCopies) {
        this.noOfCopies = noOfCopies;
    }

    public void setNoOfCopies(int noOfCopies) {
        if (noOfCopies >= 0) {
            this.noOfCopies = noOfCopies;
        }
    }

    public void increaseNoOfCopies(int copies) {
        this.setNoOfCopies(this.noOfCopies + copies);
    }

    public void decreaseNoOfCopies(int copies) {

    }
}
