<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="manifest" href="img/site.webmanifest">
	<link rel="shortcut icon" type="image/png" href="img/favicon.png"/>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="assets/style.css">
    <title>Login</title>
  </head>
  <body class="bg-custom text-light">
    <div class="container mt-5">
      <div class="row">
        <div class="col-md-6 ml-auto mr-auto">
          <div class="card bg-custom-1 mb-5">
            <h3 class="text-center">Login DashP</h3>
            <div class="card-body">
              <div class="row">
                <div class="col-md-8 ml-auto mr-auto">
                  <form action="login2.php" method = "POST">
                    <div class="form-group">
                      <label for="exampleInputEmail1">Usuari</label>
                      <input type="text" class="form-control" id="usuari" name="usuari" placeholder="Usuari">
                    </div>
                    <div class="form-group">
                      <label for="exampleInputPassword1">Contrasenya</label>
                      <input type="password" class="form-control" name="password" placeholder="Contrasenya">
                    </div>
                    <button type="submit" class="btn btn-primary">Enviar</button>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>