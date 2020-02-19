
// Program will draw some boxes 20 pixels between each rectangle, they are all
// concentric.
// Use a loop to draw the repeated rectangles.
// Window is 200 X 200

import java.util.*;
import java.awt.*;

public class Design1
{
	public static void main(String[] ars)
	{
		// Creates the drawing panel
		DrawingPanel panel = new DrawingPanel(200, 200);

		// Using the Graphics paint brush
		Graphics g = panel.getGraphics();

		// Loop that creates the rectangles
		for ( int i = 1; i <= 4; i++ )
		{
			g.drawRect(20 * i, 20 * i, 200 - 40 * i, 200 - 40 * i);
		}
	}
}
