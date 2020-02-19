package UCB;

public class Body
{
	double xxPos;
	double yyPos;
	double xxVel;
	double yyVel;
	double mass;
	String imgFileName;

	public Body(double xxpos, double yyPos, double xxVel, double yyVel, double mass, String imgFileName)
	{
		this.xxPos = xxpos;
		this.yyPos = yyPos;
		this.xxVel = xxVel;
		this.yyVel = yyVel;
		this.mass = mass;
		this.imgFileName = imgFileName;
	}

	public Body(Body b)
	{
		this.xxPos = b.xxPos;
		this.yyPos = b.yyPos;
		this.xxVel = b.xxVel;
		this.yyVel = b.yyVel;
		this.mass = b.mass;
		this.imgFileName = b.imgFileName;
	}

	public double calcDistance(Body b)
	{
		double x = Math.pow(Math.abs(b.xxPos - this.xxPos), 2);
		double y = Math.pow(Math.abs(b.yyPos - this.yyPos), 2);

		return Math.sqrt(x + y);
	}

}
