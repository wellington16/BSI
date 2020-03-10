package heran�a;

public abstract class Conta {
	protected double saldo;
	public int conta;
	
	//Overloading				
	public void sacar(double valor){
		if (this.saldo >= valor){
			this.saldo -= valor;
		}else{
			System.out.println("N�o possui saldo.");
		}
	}
	
	//Overloading
	public void sacar(double valor, String senha ){ 
		if (this.saldo >= valor){
			this.saldo -= valor;
		}else{
			System.out.println("N�o possui saldo.");
	}
	}
	
	public void sacar(){
			if (this.saldo >= 50){
				this.saldo -= 50;
	}else{
		System.out.println("N�o possui saldo.");
	}
	}
	public void depositar(double valor){
		this.saldo += valor;
	}
	
	public void verSaldo(){
		System.out.println("Saldo = R$ " + this.saldo);
	}
	
}
