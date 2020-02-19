//creates a program to animate a ball moving in the drawing panel
//I am still working on it. Will come back to it later. 

import java.awt.*;
import java.util.*;

public class Trajectory {
	//constant for earths gravitational acceleration
	public static final double ACCELERATION = -9.81;

	public static void main(String[] args) {

		intro();

		Scanner console = new Scanner(System.in);

		//get the information from the user with an interactive scanner
    	System.out.print("velocity (meters/second)? ");
    	double velocity = console.nextDouble();
    	System.out.print("angle (degrees)? ");
    	double angle = Math.toRadians(console.nextDouble());
    	System.out.print("number of steps to display? ");
    	int steps = console.nextInt();
    	System.out.println();

    	DrawingPanel panel = new DrawingPanel(600, 600);
		panel.setBackground(Color.CYAN);

		Graphics g = panel.getGraphics();

		panel.sleep(1000);
    	printTable(g, velocity, angle, steps);

	}

	public static double round2(double n) {
		return Math.round(n * 100.0) / 100.0;

	}

	public static void intro() {
		System.out.println("This program computes the");
   	    System.out.println("trajectory of a projectile given");
    	System.out.println("its initial velocity and its");
    	System.out.println("angle relative to the");
    	System.out.println("horizontal.");
    	System.out.println();
    }

    public static void printTable(Graphics g, double velocity, double angle, int steps) {
   		double xVelocity = velocity * Math.cos(angle);
		double yVelocity = velocity * Math.sin(angle);

		double totalTime = -2.0 * yVelocity / ACCELERATION;
		double timeIncrement = totalTime / steps;
		double xIncrement = xVelocity * timeIncrement;

		double x = 0.0;
		double y = 0.0;
		double t = 0.0;

		System.out.println("step\tx\ty\ttime");
		System.out.println("0\t0.0\t0.0\t0.0");

		for (int i = 1; i <= steps; i++) {
			t += timeIncrement;

			// erase last ball by coloring it white
            g.setColor(Color.WHITE);
            g.fillOval((int) x , (int) y , 10, 10);
            // draw next frame
            //x = x + xVelocity / 10.0;
            //y = y + yVelocity / 10.0;
            x += xIncrement;
			y += yVelocity * t + 0.5 * ACCELERATION * t * t;

            g.setColor(Color.BLACK);
            g.fillOval((int) x , (int) y , 10, 10);

            System.out.println(i + "\t" + round2(x) + "\t" +
			              	  round2(y) + "\t" + round2(t));

		}
	}
/*
	public static void drawBall(Graphics g, int x, int y, int steps) {
		for (int i = 1; i <= steps; i++) {
			t += timeIncrement;

			// erase last ball by coloring it white
            g.setColor(Color.WHITE);
            g.fillOval((int) x , (int) y , 10, 10);
            // draw next frame
            //x = x + xVelocity / 10.0;
            //y = y + yVelocity / 10.0;
            x += xIncrement;
			y = yVelocity * t + 0.5 * ACCELERATION * t * t;

            g.setColor(Color.BLACK);
            g.fillOval((int) x , (int) y , 10, 10);

            System.out.println(i + "\t" + round2(x) + "\t" +
			              	  round2(y) + "\t" + round2(t));

		}	
	}
*/
}

   /* // returns the vertical displacement for a body given
    // initial velocity v, elapsed time t, and acceleration a
    public static double displacement(double v, double t, double a) {
    	return v * t + 0.5 * a * t * t;
    } */







