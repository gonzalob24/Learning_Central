//Modify your Design1 class into a new class Design2 that has a method named drawDesign
//that accepts parameters for the window width and height and displays the rectangles at 
//the appropriate sizes. For example, if your drawDesign method was called with values of 300 and 100

import java.awt.*;

public class Design2 {
	public static void main(String[] args) {
  
	drawDesign(300, 300);	
  
	}

	//static method to create a panel and rectangles
	public static void drawDesign(int width, int height) {
  
		//Creates the panel
		DrawingPanel panel = new DrawingPanel(width, height);

		//Uses the graphics paint bursh
		Graphics g = panel.getGraphics();

		//Loop that draws the design
		for (int i = 1; i <= 4; i++) {
			g.drawRect(30 * i, 10 * i, width - 60 * i, height - 20 * i);
		}
	}
}
