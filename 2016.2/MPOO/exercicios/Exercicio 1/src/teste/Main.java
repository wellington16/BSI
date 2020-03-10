package teste;

import java.sql.Date;

import javax.print.attribute.standard.DateTimeAtCreation;

public class Main {
	
	public static void main (String [] args)
	{
		
		HelloWorld pessoa = new HelloWorld();
		pessoa.RetornarHoraAtual();
		pessoa.setNome("Wellington");
		pessoa.imprimir(); 
	}
}
