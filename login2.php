<?php
error_reporting(E_ERROR | E_WARNING | E_PARSE);
//ini_set('display_errors', 'On');
//error_reporting(E_ALL);

$conn = new MongoDB\Driver\Manager("mongodb://192.168.56.105:27017");
//echo "Connection to database successfull. <br>";

$filter =   ['_id' => "users"];
$option = [];
$read = new MongoDB\Driver\Query($filter, $option);
$rows = $conn->executeQuery('projecte.usuaris', $read);
$rows = $rows->toArray();

$usuari = $_POST['usuari'];
$password = $_POST['password'];
		
foreach ($rows as $r) {
	foreach ($r as $r2){
		$f1 = $r2->usuari;
		$f2 = $r2->password;
				
		if ($f1 == $_POST['usuari'] and $f2 == $_POST['password'])
		{
			$existe = true;
		}
	}
}

if($existe == true)
{
	

if (isset($_POST['usuari']) AND isset($_POST['password'])) {
	echo"<!DOCTYPE html>
			<html lang='es'>
			<head>
			  <title>DashP</title>
			  <meta charset='utf-8'>
			  <meta name='viewport' content='width=device-width, initial-scale=1'>
			  <link rel='stylesheet' href='./assets/backgroud.css'>
			  <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css'>
			  <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>
			  <link rel='shortcut icon' type='image/png' href='img/favicon.png'/>
			  <script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js'></script>
			</head>
			<body>
			<div class = 'box gradDynamic'>

			<div class='container'>
				<h3 class='text-center'>Sel·leciona una opció</h3>
				<h3 class='text-left'>Benvingut/a : $usuari</h3>
				<br>
				<a class='btn btn-secondary' href='dash01/dash01.php' role='button'> <img src='./img/1.png' height='60' width='60' alt='Un dia'>  </a>
				<a class='btn btn-secondary' href='dash02/dash02.php' role='button'><img src='./img/1.png' height='60' width='60'> <img src='./img/vs.png' height='20' width='20'> <img src='./img/1.png' height='60' width='60'> </a>
				<a class='btn btn-secondary' href='dash03/dash03.php' role='button'><img src='./img/money.png' height='60' width='60'></a>
				<a class='btn btn-secondary' href='dash04/dash04.php' role='button'><img src='./img/hora.png' height='60' width='60'></a>
				<a class='btn btn-secondary' href='http://www.dashp.cat/fase2/login.php' role='button'><img src='./img/logout.png' height='70' width='70'></a>
			</div>

			<?php
			shell_exec('taskkill /F /IM python.exe /T');
			?>

			</body>
		</html>";
}
else{
	echo"fuera";
	header("Location: http://www.dashp.cat/fase2/error.php");
	exit();
	}

}
else{
	header("Location: http://www.dashp.cat/fase2/error.php");
	exit();
}


?>