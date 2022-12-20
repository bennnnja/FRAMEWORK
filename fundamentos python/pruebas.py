import cherrypy
import random
import string

class application:
    @cherrypy.expose
    def index(self):
        return """
        <html>
        <head>
            <title>FORO</title>
        </head>
        <body>
            <h1>PRUEBA</h1>
            <h2>PRUEBA_2</h2>
            <h3>PRUEBA_3</h3>
            <p>Este es un texto de prueba</p>
            <p>
                Este texto es solo de <span style="color:cyan">prueba</span>
                para este proyecto <br><br>
                otra prueba
            </p>
            <a href="https://www.icci-unap.cl/">Ir a la pagina de ICCI UNAP</a>
            <img src="img/logounap.png"  width="400"  />
            <form>
                <label for="Nombre">Nombre</label>
                <input type="text" id="Nombre" name="Nombre" placeholder="Ingrese su nombre"/>
                <br>
                <label for="Apellido">Apellido</label>
                <input type="text" id="Apellido" name="Apellido" placeholder="Ingrese su apellido"/>
                <br>
                <label for="Email">Email</label>
                <input type="email" id="Email" name="Email" placeholder="Ingrese su email"/>
                <br>
                <label for="Contrasena">Contrasena</label>
                <input type="password" id="Contrasena" name="Contrasena" placeholder="Ingrese su contrasena"/>
            </form>
        </body>
        </html>
        """
    

if __name__ == "__main__" :
    cherrypy.quickstart(application())

        
    