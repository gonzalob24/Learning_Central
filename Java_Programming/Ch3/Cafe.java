import java.awt.*;
public class Cafe 
{
   public static void main(String[] args) 
   {
        DrawingPanel panel = new DrawingPanel(650, 400);
        Graphics g = panel.getGraphics();
		  panel.setBackground(Color.GRAY);      
        
        drawRow(g, 0, 0, 20, 4);
        drawRow(g, 50, 70, 30, 5);
        
        drawGrid(g, 10, 150, 25, 4, 4, 0);
        drawGrid(g, 250, 200, 25, 3, 3, 10);
        drawGrid(g, 400, 20, 35, 2, 2, 35);
        drawGrid(g, 425, 180, 20, 5, 5, 10);	  
   }
   
   public static void drawPair(Graphics g, int x, int y, int size) 
   {
        g.setColor(Color.BLACK);
        g.fillRect(x, y, size, size);
        g.setColor(Color.BLUE);
        g.drawLine(x, y, x+size, y+size);
        g.drawLine(x, y+size, x+size, y);
        g.setColor(Color.WHITE);
        g.fillRect(x+size, y, size, size);
   }
   
   public static void drawRow(Graphics g, int x, int y, int size, int numPairs) 
   {
        for(int i=0; i<=numPairs-1; i++) 
        {
            drawPair(g, x+2*size*i, y, size);
        }
   }

   public static void drawGrid(Graphics g, int x, int y, int size, int numHPairs, int numVPairs, int offset) 
   {
        for(int i=0; i<=numHPairs-1; i++) 
        {
            drawRow(g, x, y+2*size*i, size, numVPairs);
            drawRow(g, x+offset, y+2*size*i+size, size, numVPairs);
        }
   //The next 2 loops will draw a gray line in between every row on the grid, to emphasize the illusion's
   //effectiveness on the eyes.
        g.setColor(Color.GRAY);
        for(int j=0; j<=numHPairs-1; j++) 
        {
            g.drawLine(x, y+2*size*j+size, x+2*size*numVPairs+offset, y+2*size*j+size);
            g.drawLine(x, y+2*size*j, x+2*size*numVPairs, y+2*size*j);
        }     
        for(int k=0; k<=numHPairs-1; k++) 
        {
            g.drawLine(x+offset, y+2*size*k+2*size, x+2*size*numVPairs+offset, y+2*size*k+2*size);
        }  
   }    
}