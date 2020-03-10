package teste;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class HelloWorld {
    private String nome;
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getNome() {
        return nome;
    }
    public void imprimir() {
        System.out.print(" - Olá " + this.getNome() + ". Você acabou de fazer seu primeiro Hello World em Java. Parabéns.");
    }
    
    public void RetornarHoraAtual()
    {
    	SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss");
    	Date hora = Calendar.getInstance().getTime(); // Ou qualquer outra forma que tem
    	String dataFormatada = sdf.format(hora);
    	
        System.out.print(dataFormatada);
    }
}
