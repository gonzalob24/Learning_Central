//Program that wull draw pyramids
//Panel size is 350 X 250 
//Each pyramid is 100 X 100, white, red and blue
//Fill color	Top-left corner		# Stairs	Heigh of each stair
//  white			(0, 0)			  	10				10
//	red 			(80, 140)			5 				20
//	blue 			(220, 50) 			20 				5

import java.awt.*;

public class Pyramid {
	public static final int SIZE = 100; //can make global variable since all boxes are this size 

	public static void main(String[] args) {
		DrawingPanel panel = new DrawingPanel(350, 250);
		//panel.setBackground(Color.WHITE);
		Graphics g = panel.getGraphics();

		drawPyramid(g, 80, 140, 5, Color.RED);
		drawPyramid(g, 0, 0, 10, Color.WHITE);

	}

	public static void drawPyramid(Graphics g, int x, int y, int stairs, Color c) {

		//border for each pyramid
		g.drawRect(x, y, SIZE, SIZE);

		for (int i = 0; i < stairs; i++) {
			int height = SIZE / stairs;
			int width = height + (height * i);
			int xCoord = x + (SIZE - width) / 2;
			int yCoord = y + height * i;
			g.setColor(c);
			g.fillRect(xCoord, yCoord, width, height);
			g.setColor(Color.BLACK);
			g.drawRect(xCoord, yCoord, width, height);
		}

	}
}