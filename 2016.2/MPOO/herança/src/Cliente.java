import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

import javax.swing.JOptionPane;



public class Cliente {
	
	private String nome;
	private String email;
	private int idade;
	private OutputStreamWriter write;
	private FileWriter writer;

	
	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public int getIdade() {
		return idade;
	}

	public void setIdade(int idade) {
		this.idade = idade;
	}

	public OutputStreamWriter getWrite() {
		return write;
	}

	public void setWrite(OutputStreamWriter write) {
		this.write = write;
	}

	public String salvar() {
		File file = new File("C:\\Dados\\CadCleintes25.txt");
		if(!file.exists()){
			try {
				file.createNewFile();
				writer = new FileWriter(file);
				writer.write(this.nome + "--"+  this.email +"--"+ this.idade);
				writer.flush();
				writer.close();
			} catch (IOException e ) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}else{
			JOptionPane.showMessageDialog(null, "Já Existe um aqrquivo igual!");
		}return "Sucesso ao cadastrar";
	}

	
}
