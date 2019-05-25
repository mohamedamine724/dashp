<!DOCTYPE html>
<html lang="es">
<head>
  <title>Projecte Dashboarding</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="shortcut icon" type="image/png" href="img/favicon.png"/>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>

<div class="container">
  <h2 class="text-center">Calcul del kWh:</h2>
  <br>
  <form action="dash03_exec.php" method="POST">
    <div class="form-group">
      <label for="email">Selecciona una data:</label>
      <input type="date" class="form-control" id="data" name="data" required>
    <div class="form-group">
	<br>
    <label for="exampleFormControlSelect1">Selecciona una empresa:</label>
    <select class="form-control" id="euros" name="euros" required>
      <?php
	
		$url='https://tarifaluzhora.es/companias';
		//file_get_contents() reads remote webpage content
		$lines_string=file_get_contents($url);
		//output, you can also save it locally on the server
		 $input_lines = htmlspecialchars($lines_string);
		$output_array = [];

		preg_match_all('/\d,\d{1,9}/', $input_lines, $output_array);

		/*echo "<pre>";
		print_r($output_array);
		echo "/<pre>";*/

		foreach ($output_array as $valor) {
			foreach ($valor as $v)
			{
				$v = str_replace(",",".",$v);
				//echo $v;
				echo "<option>$v</option>";
				echo "<br>";
			}
			//$valor = str_replace(",",".",$valor);
			
		}



?>
    </select>
  </div>
  <br>
    <button type="submit" class="btn btn-default" name="enviar">Crear el Dash</button>
	<input type="reset"  class="btn btn-default" value="Esborrar">
	
	<br>
	  <!-- Modal -->
  <div class="modal fade" id="myModal" role="dialog">
    <div class="modal-dialog">
      <!-- Modal content-->
      <div class="modal-content">
        <div class="modal-body">
          <p>Creant el servidor de Dash.... (Pot trigar uns minuts)</p>
        </div>
        <div class="modal-footer">
		  <a class="btn btn-primary" href="http://127.0.0.1:8050" target="_blank" role="button">Obrir el Dash<a>
        </div>
      </div>
      
    </div>
  </div>
	<br>
	<br>
	<a class="btn btn-primary" role="button" data-target="#myModal" data-toggle="modal">Obrir el Dash<a>
  </form>
  
  
 <br>
 <br>
  
	<div class="alert alert-danger" role="alert">
		Per obrir un altre Dash, s'ha de pressionar la tecla ESC i tornar a emplenar el formulari..
	</div>
	
	
	<br>
	<br>
	<!--<button class="btn"><a class="btn" href = "../login2.php"><i class="fa fa-home"></i></a></button>-->
</div>

<?php
shell_exec("taskkill /F /IM python.exe /T");
?>

</body>
</html>



