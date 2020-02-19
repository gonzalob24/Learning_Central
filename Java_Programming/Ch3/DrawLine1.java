import java.awt.*;  // For the graphics

public class DrawLine1 {
	public static void main(String[] args) {

		//Create the drawing panel
		DrawingPanel panel = new DrawingPanel(200, 100);  //first object

		//Draw a line on the drawing panel
		//Using the graphics paint brush

		Graphics g = panel.getGraphics();  //second object

		g.drawLine(25, 75, 175, 25);
	}
}

