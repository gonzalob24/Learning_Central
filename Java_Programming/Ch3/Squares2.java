//Modify your Squares program from the previous exercise into a new class Squares2 that draws
//the same figure muliple times across the panel
//Drawing panel is now 400 X 300. Figure positions (50, 50), (250, 10) and (180, 115)
//Use one or more parameterized static methods to reduce the redundancy of your solution.

import java.awt.*;

public class Squares2 {
	public static void main(String[] args) {
		//Creates the drawing panel
		DrawingPanel panel = new DrawingPanel(400, 300);

		//sets the background color
		panel.setBackground(Color.CYAN);

		//Gets the paint brush to draw on the panel
		Graphics g = panel.getGraphics();

		drawSquares(g, Color.RED, Color.BLACK, 50, 50);
		drawSquares(g, Color.RED, Color.BLACK, 250, 10);
		drawSquares(g, Color.RED, Color.BLACK, 180, 115);	
	}

	//Static method that draws the squares depending on colo and location. All are the same size
	public static void drawSquares(Graphics g, Color square, Color line, int x, int y) {
		for (int i = 1; i <= 5; i++) {
			g.setColor(square);
			g.drawRect(x, y, 20 * i, 20 * i);
		}
		g.setColor(line);
		g.drawLine(x, y, x + 20 * 5, y + 20 * 5);
	}
}
