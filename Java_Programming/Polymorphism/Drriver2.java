public class Drriver2 
{
	public static void main(String[] args)
	{
	
		GameObject player = new Player();
		GameObject menu = new Menu();
		
		//call the method it will not find it b/c
		//the method is inside Player class and not GameObject
		//you can cast it
		//((Player) player).someMethod();
		//menu.draw();
		
		//declare an array of gameObjects and 
		
		//you can instantiate the PLayer and menu here or
		//or above like in first 2 lines
		GameObject[] gameObjects = new GameObject[2];
		gameObjects[0] = player;
		gameObjects[1] = menu;
		
		for(GameObject obj : gameObjects)
		{
			obj.draw();
		}
	}
}
