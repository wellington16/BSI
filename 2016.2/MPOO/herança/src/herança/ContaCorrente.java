package herança;

public class ContaCorrente extends Conta{
	
	public void sacar(double valor){
		super.sacar(valor);
		this.juro();
		}
	private void juro(){
			this.saldo -=1;
		}

}
