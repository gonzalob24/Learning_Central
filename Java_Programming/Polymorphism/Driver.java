
public class Driver 
{
	public static void main(String[] args)
	{
		/*
		GameObject player = new Player();
		GameObject menu = new Menu();
		
		//call the method
		player.draw();
		menu.draw();
		*/
		//declare an array of gameObjects and 
		
		//you can instantiate the PLayer and menu here or
		//or above like in first 2 lines
		GameObject[] gameObjects = new GameObject[2];
		gameObjects[0] = new Player();
		gameObjects[1] = new Menu();
		
		for(GameObject obj : gameObjects)
		{
			obj.draw();
		}
	}
}
