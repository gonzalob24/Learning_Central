//modified version of the previous Stairs program.
//The staris are going to be upside down

import java.awt.*;

public class Stairs2 {
	public static void main(String[] args) {
		DrawingPanel panel = new DrawingPanel(110, 110);
		Graphics g = panel.getGraphics();

		for (int i = 0; i < 10; i++) {
			g.drawRect(5, 5 + i * 10, 100 - i * 10, 10);
		}
	}
}
