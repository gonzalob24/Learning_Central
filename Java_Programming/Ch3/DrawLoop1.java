import java.awt.*;

public class DrawLoop1 {
	public static void main(String[] args) {

		//Create the panel
		DrawingPanel panel = new DrawingPanel(200, 100);

		//Set panel backgrounf color
		panel.setBackground(Color.CYAN);

		Graphics g = panel.getGraphics();
		for (int i = 0; i <= 4; i++) {
			g.setColor(Color.WHITE);
			g.fillOval(i * 50, i * 25, 50, 25);
			g.setColor(Color.BLACK);
			g.drawRect(i * 50, i * 25, 50, 25);

		}

	}
}