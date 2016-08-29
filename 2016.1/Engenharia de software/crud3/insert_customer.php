<?php

echo "You are on the inser_customer.php file";

  $pnome=  $_POST['primero_nome'];
  $Unome= $_POST['ultimo_nome'];
  $idade= $_POST['idade'];
  $email=  $_POST['email'];

  echo $pnome."<br/>";
  echo $Unome."<br/>";
  echo $idade."<br/>";
  echo $email."<br/>";
  
	//1 CRIANDO A CONECÇÃO COM O DATABASE
  $conecta = mysql_connect("LOCALHOST", "root", "") or print (mysql_error()); 
	print "Conexão OK!"; 
	mysql_close($conecta);
  //2 SELECT O USUARIO DO DATABASE
  #mysql_select_db('alunobd') or die("não conseguiu conectar com tabela");
  
  echo ' você conseguiu gravar com sucesso.:)'
  
  
?>