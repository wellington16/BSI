package herança;

import javax.swing.JOptionPane;



public class Principal {
	public static void main(String[] args) {
		
		ContaCorrente c = new ContaCorrente();
		c.depositar(100);
		c.sacar(50);
		
		c.verSaldo();
		
		ContaPoupança p = new ContaPoupança();
		p.depositar(100);
		p.sacar(50);
		p.verSaldo();
		
		
		String acao = JOptionPane.showInputDialog("Digite o tipo de conta");
		IDb db;
		if (acao.equals("m")){
			db = new MySQL();
			db.conectar();
			db.desconectar();
		}else{
			db = new Oracle();
			db.conectar();
			db.desconectar();
		}
	}

}
