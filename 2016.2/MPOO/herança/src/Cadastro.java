import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;


public class Cadastro {

	private JFrame frame;
	private JTextField tfNome;
	private JTextField tfEmail;
	private JTextField tfIdade;
	private JButton btnNewButton;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Cadastro window = new Cadastro();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public Cadastro() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 368, 158);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		JLabel lblNome = new JLabel("Nome :");
		lblNome.setBounds(10, 11, 46, 14);
		frame.getContentPane().add(lblNome);
		
		tfNome = new JTextField();
		tfNome.setBounds(66, 8, 261, 20);
		frame.getContentPane().add(tfNome);
		tfNome.setColumns(10);
		
		JLabel lblEmail = new JLabel("Email :");
		lblEmail.setBounds(10, 36, 46, 14);
		frame.getContentPane().add(lblEmail);
		
		tfEmail = new JTextField();
		tfEmail.setBounds(66, 33, 261, 20);
		frame.getContentPane().add(tfEmail);
		tfEmail.setColumns(10);
		
		JButton btnCadastar = new JButton("Cadastar");
		btnCadastar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				Cliente cliente = new Cliente();
				cliente.setNome(tfNome.getText());
				cliente.setEmail(tfEmail.getText());
				cliente.setIdade(Integer.parseInt(tfIdade.getText()));
				JOptionPane.showMessageDialog(null, cliente.salvar());			
			}
		});
		btnCadastar.setBounds(205, 90, 122, 23);
		frame.getContentPane().add(btnCadastar);
		
		JLabel lblDataNasc = new JLabel("Data Nasc.:");
		lblDataNasc.setBounds(10, 61, 59, 14);
		frame.getContentPane().add(lblDataNasc);
		
		tfIdade = new JTextField();
		tfIdade.setBounds(66, 58, 261, 20);
		frame.getContentPane().add(tfIdade);
		tfIdade.setColumns(10);
		
		btnNewButton = new JButton("Cancelar");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
		btnNewButton.setBounds(66, 90, 129, 23);
		frame.getContentPane().add(btnNewButton);
	}
}
