import java.awt.*;

public class CafeWall {
	public static void main(String[] args) {
		
		//create the panel
		DrawingPanel mortar = new DrawingPanel(650, 400);
		Graphics g = mortar.getGraphics();
		mortar.setBackground(Color.GRAY);
		
		//paramters for each individual grid set arranged as follows:
		//x coordinates, y coordinate, number of pairs, size of each
		//square, number of rows, degree of offest
		drawGrid(g, 0, 0, 4, 20, 0, 0);
		drawGrid(g, 50, 70, 5, 30, 1, 0);
		drawGrid(g, 10, 150, 4, 25, 8, 0);
		drawGrid(g, 250, 200, 3, 25, 6, 10);
		drawGrid(g, 425, 180, 5, 20, 10, 10);
		drawGrid(g, 400, 20, 2, 35, 4, 35);
	}
	
	//method for arranging grids based on paramter inputs
	public static void drawGrid(Graphics g, int x, int y, int pairs, int size, int numberOfRows, int offset) {
		for (int r = 0; r < numberOfRows; r++) {
			int shift = r % 2 * offset;
			for (int i = 0; i < pairs; i++) {
				g.setColor(Color.BLACK);
				g.fillRect(i * 2 * size + x + shift, r * size + y + r * 2, size, size);
				g.setColor(Color.BLUE);
				g.drawLine(i * 2 * size + x + shift, r * size + y + r * 2, i * 2 * size + x + size + shift, r * size + y + r * 2 + size);
				g.drawLine(i * 2 * size + x + size + shift, r * size + y + r * 2, i * 2 * size + x + shift, r * size + y + r * 2 + size);  
				g.setColor(Color.WHITE);
				g.fillRect(i * 2 * size + size + x + shift, r * size + y + r * 2, size, size);
			}
		}
	}
}