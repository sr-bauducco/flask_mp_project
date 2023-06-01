from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>okok</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    header {
      background-color: #000;
      color: #fff;
      padding: 20px;
      text-align: center;
    }
    h1 {
      margin: 0;
    }
    main {
      padding: 20px;
      text-align: center;
    }
  </style>
</head>
<body>
  <header>
    <h1>Welcome to My Awesome Website</h1>
  </header>
  <main>
    <h2>About</h2>
    <p>This is a fantastic website created using HTML5.</p>
    <h2>Contact</h2>
    <p>You can reach us at info@example.com.</p>
  </main>
</body>
</html>
"""

@app.route("/login")
def login():
    return """<!DOCTYPE html>
<html>
<head>
  <title>Menu</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }

    header {
      background-color: #333;
      padding: 10px;
      color: #fff;
      text-align: center;
    }

    nav {
      background-color: #f2f2f2;
      padding: 10px;
    }

    nav ul {
      list-style-type: none;
      margin: 0;
      padding: 0;
    }

    nav ul li {
      display: inline;
      margin-right: 10px;
    }

    nav ul li a {
      text-decoration: none;
      color: #333;
      padding: 5px;
    }

    nav ul li a:hover {
      background-color: #333;
      color: #fff;
    }
  </style>
</head>
<body>
  <header>
    <h1>Meu Menu</h1>
  </header>

  <nav>
    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="#">Sobre</a></li>
      <li><a href="#">Contato</a></li>
    </ul>
  </nav>

  <main>
    <!-- Conteúdo principal da página -->
  </main>
</body>
</html>
"""