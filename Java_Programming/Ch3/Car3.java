// This variation of the Car program uses a parameterized method to draw seven
// different cars on a DrawingPanel.  It includes not only parameters for
// location (x, y), but also a parameter for size.  Five of the cars are
// produced using a for loop in main.

import java.awt.*;

public class Car3 {
    public static void main(String[] args) {
        DrawingPanel panel = new DrawingPanel(400, 200);
        panel.setBackground(Color.LIGHT_GRAY);
        
        Graphics g = panel.getGraphics();
        drawCar(g, 10, 30, 100);
        drawCar(g, 150, 10, 50);

        for (int i = 0; i < 5; i++) {
            drawCar(g, 10 + i * 50, 130, 40);
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
