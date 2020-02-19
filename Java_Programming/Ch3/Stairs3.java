//modified version of previosu Stairs programs

import java.awt.*;

public class Stairs3 {
	public static void main(String[] args) {
		DrawingPanel panel = new DrawingPanel(110, 110);
		Graphics g = panel.getGraphics();

		for (int i = 0; i < 10; i++) {
			g.drawRect(95 - i * 10, 5 + i * 10, 10 + i * 10, 10);
		}
	}
}
