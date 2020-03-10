
public class DesafioContarClass {
	private static int ContadorObjetos;

	public static int getContadorObjetos() {
		return ContadorObjetos;
	}

	DesafioContarClass ()
	{
		IncrementarObjetos();
	}
	
	public static int IncrementarObjetos()
	{
		return ContadorObjetos++;
	}
}
