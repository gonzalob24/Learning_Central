import java.awt.*;

public class DrawMessage1 {
	public static void main(String[] args) {
		DrawingPanel panel = new DrawingPanel(300, 200);

		panel.setBackground(Color.YELLOW);

		Graphics g = panel.getGraphics();

		drawText(g);
	}

	public static void drawText(Graphics g) {
		for (int i = 0; i < 10; i++) {
			g.drawString("The is no place like AI", i * 5, 10 + i * 10);
		}
	}
}