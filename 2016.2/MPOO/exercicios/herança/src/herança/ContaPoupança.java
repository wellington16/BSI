package herança;

public class ContaPoupança extends Conta{

	
	public void depositar(double valor){
		super.depositar(valor);
		this.juro();
	}
	private void juro(){
		this.saldo +=1;
	}

}
