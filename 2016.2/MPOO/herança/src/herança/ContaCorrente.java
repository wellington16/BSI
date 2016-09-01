package herança;

public class ContaCorrente extends Conta{
	
	@Override
	public void sacar(double valor){
		super.sacar(valor);
		this.juro();
		}
	@Override
	public void sacar(double valor, String senha ){
		if (senha == "123"){
			if (this.saldo >= valor){
				this.saldo -= valor;
			}else{
				System.out.println("Não possui saldo.");
		}
		}
	}
	
	private void juro(){
			this.saldo -=1;
		}

}
