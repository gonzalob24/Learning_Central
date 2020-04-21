package SortingAlgorithms;

// Node class
public class B4Node 
{
    // array to store the keys
    public int[] keys;
    // Degree of the tree
    public static final int DEG = 4;
    
    // array to store the child pointers
    public B4Node[] ch; 
    
    // number of keys
    public int num_keys; 
    
    // will be true or false when checking for leaf node
    public boolean checkIfLeaf; 
  
    // Constructor to set a BTree object
    B4Node(boolean checkIfLeaf) 
    { 
        this.checkIfLeaf = checkIfLeaf; 
        this.ch = new B4Node[2 * DEG]; 
        this.num_keys = 0; 
        this.keys = new int[2 * DEG - 1]; 
        
    } 
  
    // Inorder traversal to show the tree is in sorted order 
    public void inorderTraversal() 
    { 
        // travers the number of keys 
        int i = 0; 
        for (i = 0; i < this.num_keys; i++) 
        {             
            // check if its a leaf or not. If flase print keys
            if (this.checkIfLeaf == false) 
            { 
                // go through the children as wekk to print keys
                ch[i].inorderTraversal(); 
            } 
            System.out.print(keys[i] + " "); 
        } 
  
        // look at the leafs and print child keys 
        if (checkIfLeaf == false) 
            ch[i].inorderTraversal(); 
    } 
    
    // method that will split child Node like in 2-3-4 tree
    public void splitChNode(int i, B4Node n)
    {
        // Create a new node to store 3 keys
        B4Node temp = new B4Node(n.checkIfLeaf);
        temp.num_keys = DEG - 1;

        // Copy keys n to temp
        for (int j = 0; j < DEG-1; j++)
            temp.keys[j] = n.keys[j+DEG];

        // children of n to temp
        if (n.checkIfLeaf == false)
        {
            for (int j = 0; j < DEG; j++)
                temp.ch[j] = n.ch[j+DEG];
        }

        // Decrement the keys in n
        n.num_keys = DEG - 1;

        // make space for the new child
        for (int j = num_keys; j >= i+1; j--)
            ch[j+1] = ch[j];

        // Link child and node
        ch[i+1] = temp;

        //Find location of new key 
        // and move larger keys one space forward
        for (int j = num_keys-1; j >= i; j--)
            keys[j+1] = keys[j];

        // Copy middle key in to node
        keys[i] = n.keys[DEG-1];

        // keep trackpf the number of keys
        num_keys++;
    }
    
    // method that will insert values to the Tree
    public void insert(int data)
    {
        // get location of where to insert data
        int i = num_keys - 1;

        // check if its a leaf or not
        if (checkIfLeaf == true)
        {
            // Finds location of where to insert new key
            // Again move larger keys forward
            while (i >= 0 && keys[i] > data)
            {
                keys[i+1] = keys[i];
                i--;
            }

            // Insert new key
            keys[i+1] = data;
            //increment number of keys
            num_keys++;
        }
        else // node is not a leaf
        {
            // look for child
            while (i >= 0 && keys[i] > data)
                i--;

            // Check if its full
            if (ch[i+1].num_keys == 2 * DEG - 1)
            {
                // If ch is full split it like in 2-3-4 tree
                splitChNode(i+1, ch[i+1]);

                // The middle key of ch[i] goes up after the split
                if (keys[i+1] < data)
                    i++;
            }
            ch[i+1].insert(data);
        }
    } 
 }