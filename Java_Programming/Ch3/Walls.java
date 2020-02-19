//Panel is 650 X 400, gray background. 
//Stand alone
//Description 		(x, y) position 	Number of pairs		Size of each box
//upper­left				(0, 0)				4	  				20
//mid­left				  (50, 70)			5					  30
//
//
//Other boxes
//Description		(x, y) position		Number of pairs		Size of each box 	2nd row offset
//lower left			(10, 150)		        	4				          	25					  0
//lower middle		(250, 200)		      	3				          	25				  	10
//lower right			(425, 180)		      	5				          	20					  10
//upper right			(400, 20)			        2				          	35					  35

import java.awt.*;

public class Walls {

//The size of the layer between each row 
public static final int MORTAR = 2;

	public static void main(String[] args) {
		//Creates the drawing panel
		DrawingPanel panel = new DrawingPanel(650, 400);

		//set the pane background
		panel.setBackground(Color.GRAY);

		//Gets the paint brush to draw on the panel
		Graphics g = panel.getGraphics();

		drawPairs(g, 0, 0, 4, 20);
		drawPairs(g, 50, 70, 5, 30);
		drawGrid(g, 10, 150, 4, 25, 0);
		drawGrid(g, 250, 200, 3, 25, 10);
		drawGrid(g, 425, 180, 5, 20, 10);
		drawGrid(g, 400, 20, 2, 35, 35);

	}

	//Static method that will draw pairs of a stand alone wall
	//boxSize the sixe of the boxes
	//x and y are the starting positions
	//pairs are the number of pairs for black and white boxes
	public static void drawPairs(Graphics g, int x, int y, int pairs, int boxSize) {

		//Loop that iterates the number of pairs specified in the parameter. 
		for (int i = 1; i <= pairs; i++) {
			g.setColor(Color.BLACK);
			g.fillRect(x, y, boxSize, boxSize);
			g.setColor(Color.BLUE);
			g.drawLine(x, y, x + boxSize, y + boxSize);
			g.drawLine(x, y + boxSize, x + boxSize, y);
			g.setColor(Color.WHITE);
			g.fillRect(x + boxSize, y, boxSize, boxSize);	
			
			//updates the x position after the initial value is used
			x += boxSize * 2;			
		}
	}

	//Static method that creates a grid of walls with spaces and shifts the second row to the right
	public static void drawGrid(Graphics g, int x, int y, int pairs, int boxSize, int offset) {
		for (int i = 1; i <= pairs; i++) {
			drawPairs(g, x, y, pairs, boxSize);
			y += boxSize + MORTAR - 1;    //Updates the y position to include the mortar
			drawPairs(g, x + offset, y, pairs, boxSize);
			y += boxSize + MORTAR - 1;    //Updates the y position to include the mortar
		}
	}
} 

































