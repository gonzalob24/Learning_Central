//Using the DrawingPanel class, write a Java class named Triangle that produces
//size: 600x200
//background color: yellow
//line color: blue
//vertical spacing between lines: 10 px
//The diagonal lines connect at the bottom in the middle.

import java.awt.*;

public class Triangle1 {
	public static void main(String[] args) {
		DrawingPanel panel = new DrawingPanel(600, 200);
		panel.setBackground(Color.YELLOW);

		Graphics g = panel.getGraphics();
		g.setColor(Color.BLUE);
		g.drawLine(0, 0, 300, 200);
		g.drawLine(600, 0, 300, 200);

		for ( int i = 0; i < 19; i++) {
			g.drawLine(15 + i * 15, 10 + i * 10, 585 - i * 15, 10 + i * 10);
		}

	}
}
