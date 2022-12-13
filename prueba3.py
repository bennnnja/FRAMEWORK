import cherrypy
import random
import string

class Generator(object):
    @cherrypy.expose
    def index(self):
        return"""
        <div align="center">
        </div>
        <h1 align="center">=========================================================================== </h1>
        <h1 align="center"> FORO </h1>
        <div align="center">
        </div>
        <div align="center">
        <img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green">
        </div>
        <div align="center">
        </div>
        <h1 align="center">=========================================================================== </h1>
        <form method="get" action="generate">
        <input type="text" value="10" name="length" />
        <button type="prueba2">Let it rain!</button>
        <tittle>Saludos</title>
        <body>
        Ingrese su nombre
        <input type="text" name"nombre"/>
        <input type="submit"/>
        </form>
        </body>
        """
    @cherrypy.expose
    def generate(self, length=10):
        return''.join(random.sample(string.hexdigits, int(length)))  

if __name__ == "__main__" :
    cherrypy.quickstart(Generator())