// Simple drawing program that draws a single car on a drawing panel.

import java.awt.*;

public class Car1 
{
    public static void main(String[] args) 
    {
        DrawingPanel panel = new DrawingPanel(400, 200);
        panel.setBackground(Color.LIGHT_GRAY);
        Graphics g = panel.getGraphics();
        
        g.setColor(Color.BLACK);
        g.fillRect(10, 30, 100, 50);
        
        g.setColor(Color.RED);
        g.fillOval(20, 70, 20, 20);
        g.fillOval(80, 70, 20, 20);
        
        g.setColor(Color.CYAN);
        g.fillRect(80, 40, 30, 20);
    }
}
