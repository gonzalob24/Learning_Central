package SortingAlgorithms;
import  java.util.Random;

 
public class BTree4 
{ 
    
    // root node pointer 
    private B4Node root;
    // Minimum degree 4
    public static final int DEG = 4;  
  
    // set an empty B Tree object 
    public BTree4() 
    { 
        this.root = null; 
    } 
  
    // method to display the tree 
    public void printTree() 
    { 
        if (this.root != null) 
            this.root.inorderTraversal(); 
        System.out.println(); 
    } 
    
    // method that will add an item to the tree
    public void add(int data_key)
    {
        if (root == null)
        {
            // set root with data
            root = new B4Node(true);
            root.keys[0] = data_key;
            // keep track of the count
            root.num_keys = 1; 
        }
        else
        {
            // root is not null
            if (root.num_keys == 2 * DEG - 1)
            {
                B4Node temp = new B4Node(false);
                
                //mode root down as child
                temp.ch[0] = root;
                
                //split root
                temp.splitChNode(0, root);
                
                // the root node now ahs to children
                int n = 0;
                if (temp.keys[0] < data_key)
                {
                    n++;
                }
                temp.ch[n].insert(data_key);
                
                // update root
                root = temp;
            }
            else 
            {
                // root is not full yet
                root.insert(data_key);
            }
        }
    }
} 