package UCB.Project1;

public class DIntNode<Any>
{
	public DIntNode<Any> prev;
	public Any item;
	public DIntNode<Any> next;

	public DIntNode(Any item, DIntNode prev, DIntNode next)
	{
		this.prev = prev;
		this.item = item;
		this.next = next;
	}
}
