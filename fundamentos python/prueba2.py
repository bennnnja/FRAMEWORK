import cherrypy
import random
import string

class Home:
    @cherrypy.expose
    def index(self):
        return"<a href='/links'>Rutas</a"     
    
    @cherrypy.expose
    def links(self):
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
        <ul>
            <li><a href='/'>Home</a></li>
            <li><a href='/contact'>Contact</a></li>
            <li><a href='/information'>Information</a></li>
            <li><a href='/generate'>Generate</a></li>
            <li><a href='/icci'>Icci</a></li>
            
        """ 

    @cherrypy.expose
    def contact(self):
        return"<a href='/links'>Rutas</a" 
    
    @cherrypy.expose
    def icci(self):
        return "https://www.inf.unap.cl/index.php/tag/unap/"     

    @cherrypy.expose
    def information(self):
        return"<a href='/links'>Rutas</a"

    @cherrypy.expose
    def generate(self, length=10):
        return''.join(random.sample(string.hexdigits, int(length)))  

cherrypy.quickstart(Home())         