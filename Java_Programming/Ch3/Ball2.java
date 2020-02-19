// This program animates a ball bouncing around in a DrawingPanel.

import java.awt.*;
import java.util.*;

public class Ball2 {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("velocity? ");
        double velocity = console.nextDouble();  // pixels per second
        System.out.print("angle   ? ");
        double angle = console.nextDouble();
        System.out.print("seconds ? ");
        int seconds = console.nextInt();
                                
        double xVelocity =  velocity * Math.cos(Math.toRadians(angle));
        double yVelocity = -velocity * Math.sin(Math.toRadians(angle));
                
        DrawingPanel p = new DrawingPanel(600, 600);
        p.setBackground(Color.CYAN);
        Graphics g = p.getGraphics();
                
        g.fillOval(295, 295, 10, 10);
        p.sleep(1000);
        double x = 300.0;
        double y = 300.0;
        for (int i = 1; i <= 10 * seconds; i++) {
            g.setColor(Color.WHITE);
            g.fillOval((int) x - 5, (int) y - 5, 10, 10);
            x = x + xVelocity / 10.0;
            y = y + yVelocity / 10.0;
            if (x <= 5 || x >= 595) {
                xVelocity = -xVelocity;
            }
            if (y <= 5 || y >= 595) {
                yVelocity = -yVelocity;
            }
            g.setColor(Color.BLACK);
            g.fillOval((int) x - 5, (int) y - 5, 10, 10);
            p.sleep(100);
        }
    }
}