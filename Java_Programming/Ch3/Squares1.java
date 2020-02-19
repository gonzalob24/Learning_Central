//Program will display a series of squares with a diagonal line from the top 
//left corner to bottom right corner.
//Drawing panel is 300 X 200, background is CYAN, the squares are in red and diagonal line is black
//line starts at (50, 50), successive horizontal and vertical lines are 20 pixels apart. 
//The diagonal line is drawn on top of the other lines. 	

import java.awt.*;

public class Squares1 {
	public static void main (String[] ars) {
		//Creates the panel
		DrawingPanel panel = new DrawingPanel(300, 200);

		//Sets the panel background color
		panel.setBackground(Color.CYAN);

		//Get the graphics paint bruch to draw on the panel
		Graphics g = panel.getGraphics();

		g.setColor(Color.RED);
		g.drawRect(50, 50, 20, 20);
		g.drawRect(50, 50, 40, 40);

		for (int i = 1; i <= 5; i++) {
			g.setColor(Color.RED);
			g.drawRect(50, 50, 20 * i, 20 * i);
		}
		g.setColor(Color.BLACK);
		g.drawLine(50, 50, 150, 150);
	}
} 
