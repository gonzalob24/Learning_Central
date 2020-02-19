//modified version of previosu Stairs programs

import java.awt.*;

public class Stairs4 {
	public static void main(String[] args) {
		DrawingPanel panel = new DrawingPanel(110, 110);
		Graphics g = panel.getGraphics();

		for (int i = 0; i < 10; i++) {
			g.drawRect(5 + i * 10, 5 + i * 10, 100 - i * 10, 10);
		}
		g.drawLine(105, 5, 105, 105);
	}
}
