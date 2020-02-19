//Modify your Squares2 program from the previous exercise into a new class Squares3 that draws 
//The smae figure of diffent sizes. Parameterize your program so that the figures have different sizes 
//The top-right figure has size 50, and the bottom-right figure has size 180 and left size 100

import java.awt.*;

public class Squares3 {
	public static void main(String[] args) {
		//Draws the panel
		DrawingPanel panel = new DrawingPanel(400, 300);

		//Sets the panel background color
		panel.setBackground(Color.CYAN);

		//Gets the paint brush do draw on the panel
		Graphics g = panel.getGraphics();

		drawSquares(g, Color.RED, Color.BLACK, 50, 50, 100);
		drawSquares(g, Color.RED, Color.BLACK, 250, 10, 50);
		drawSquares(g, Color.RED, Color.BLACK, 180, 115, 180);

	}

	//Static method that draws the squares depending on size locaton and color
	public static void drawSquares(Graphics g, Color squares, Color line, int x, int y, int size) {
		for (int i = 1; i <= 5; i++) {
			g.setColor(squares);
			g.drawRect(x, size / 5, (size / 5) * i, (size / 5) * i);
		}
		g.setColor(line);
		g.drawLine(x, y, x + size , y + size );
	}
}
