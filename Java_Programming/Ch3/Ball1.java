// This program animates a ball moving at a particular angle and with
// a particular velocity.

import java.awt.*;

public class Ball1 {
    public static void main(String[] args) {
        double velocity = 25.7;  // pixels per second
        double angle = 45.0;
        int seconds = 15;
                
        double xVelocity =  velocity * Math.cos(Math.toRadians(angle));
        double yVelocity = -velocity * Math.sin(Math.toRadians(angle));
                
        DrawingPanel p = new DrawingPanel(600, 600);
        p.setBackground(Color.CYAN);
        Graphics g = p.getGraphics();

        // draw initial ball
        g.fillOval(300, 300, 10, 10);
        p.sleep(1000);

        double x = 300.0;
        double y = 300.0;
        for (int i = 1; i <= 10 * seconds; i++) {
            // erase last ball by coloring it white
            g.setColor(Color.WHITE);
            g.fillOval((int) x , (int) y , 10, 10);
            // draw next frame
            x = x + xVelocity / 10.0;
            y = y + yVelocity / 10.0;
            g.setColor(Color.BLACK);
            g.fillOval((int) x , (int) y , 10, 10);

            p.sleep(100);
        }
    }
}
