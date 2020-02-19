// This variation of the Car program uses a parameterized method to draw an
// animation of a moving car by drawing it 300 times, increasing its
// x-coordinate by one each time.  It uses the DrawingPanel's clear method to
// erase the previous drawing and the panel's sleep method to have the program
// pause (otherwise the drawing happens too quickly for the human eye to
// properly perceive what is happening).

import java.awt.*;

public class Car4 {
    public static void main(String[] args) {
        DrawingPanel panel = new DrawingPanel(400, 200);
        panel.setBackground(Color.LIGHT_GRAY);
        
        Graphics g = panel.getGraphics();

        for (int i = 0; i < 300; i++) {
            panel.clear();
            drawCar(g, 10 + i, 130, 40);
            panel.sleep(10);  // pause for 10 milliseconds
        }
    }
    
    // Draws a car figure using the given Graphics object with upper-left
    // corner (x, y) and given size
    public static void drawCar(Graphics g, int x, int y, int size) {
        g.setColor(Color.BLACK);
        g.fillRect(x, y, size, size / 2);
        
        g.setColor(Color.RED);
        g.fillOval(x + size / 10, y + 2 * size / 5, size / 5, size / 5);
        g.fillOval(x + 7 * size / 10, y + 2 * size / 5, size / 5, size / 5);
        
        g.setColor(Color.CYAN);
        g.fillRect(x + 7 * size / 10, y + size / 10, 3 * size / 10, size / 5);
    }
}
