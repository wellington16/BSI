package heranša;

public class Principal {
	public static void main(String[] args) {
		
		ContaCorrente c = new ContaCorrente();
		c.depositar(100);
		c.sacar(50);
		
		c.verSaldo();
		
		ContaPoupanša p = new ContaPoupanša();
		p.depositar(100);
		p.sacar(50);
		p.verSaldo();
	}

}
