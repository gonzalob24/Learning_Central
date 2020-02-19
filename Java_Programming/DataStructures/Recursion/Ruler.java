/*
 * PROGRAMMER: Gonzalo Betancourt
 * 
 * COURSE: CSCI 2315-02 Data Structures
 * 
 * DATE: October 2, 2019
 * 
 * ASSIGNMENT: Homework #3
 * 
 * ENVIRONMENT: Mac OS, Windows or Linux
 * 
 * FILES INCLUDED: Program Solving document, screen shot of working code and
 * Ruler source file
 * 
 * PURPOSE: run the code that will draw an image of a ruler
 * 
 * PRECONDITIONS: use positive number for the lengths of the lines drawn
 * 
 * OUTPUT: output will be an image of a ruler
 * 
 * ALGORITHM: use the Graphics library to draw on the canvas
 * perform a recursive search until the level is less than 1, starts at 80
 * update the left and right positions after each recursive call
 * 
 * 
 * EXAMPLE: a ruler
 * 
 * 
 */

package Recursion;

import java.awt.Frame;
import java.awt.Graphics;

public class Ruler extends Frame

{
	private static final int theSize = 511;

	public void paint(Graphics g)
	{
		drawRuler(g, 10, theSize - 1 + 10, 8);
	}

	private void drawRuler(Graphics g, int left, int right, int level)
	{
		if (level < 1)
			return;
		int mid = (left + right) / 2;
		// *************
		// **** drawing in slow motion
		try
		{
			Thread.sleep(300);
		}// try with 1000
		catch (InterruptedException e)
		{
		}
		// *************/
		g.drawLine(mid, 80, mid, 80 - level * 5);
		drawRuler(g, left, mid - 1, level - 1);
		drawRuler(g, mid + 1, right, level - 1);
	}

	// Simple test program
	// For simplicity, must terminate from console
	public static void main(String[] args)
	{
		Frame f = new Ruler();
		f.setSize(theSize + 20, 110);
		f.setVisible(true);
	}
}