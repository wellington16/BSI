package heran�a;

public class Conta {
	protected double saldo;
	public int conta;
				
	public void sacar(double valor){
		if (this.saldo >= valor){
			this.saldo -= valor;
		}

	}
	public void depositar(double valor){
		this.saldo += valor;
	}
	
	public void verSaldo(){
		System.out.println("Saldo = R$ " + this.saldo);
	}
	
}
