import cherrypy
import random
import string

class HolaMundo(object):
    @cherrypy.expose
    def index(self):
        return'Hola Mundo'

    @cherrypy.expose
    def generate(self):
        return''.join(random.sample(string.hexdigits, 10))
    

##if __name__ == "__main__" :
    ##cherrypy.quickstart(HolaMundo())

        
    