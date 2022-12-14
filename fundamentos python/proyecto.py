import cherrypy
import string
import pyodbc

class Home:
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
        <ul>
        <div align="center">
        <img src="data:image/jpeg;base64,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" />
        <h1 align="center"> Bienvenido a FORO </h1> 
        </div>
        </html>
        </body>
            <form action="Validar">
                <h2>Registrarse</h2>
                <label for="Nombre">Nombre</label>
                <input type="text" name="nombre" placeholder="Ingrese su nombre"/>  
                <br>
                <label for="Apellido">Apellido</label>
                <input type="text" name="apellido" placeholder="Ingrese su apellido"/> 
                <br>
                <label for="Email">Email</label>
                <input type="email" name="email" placeholder="Ingrese su email"/>   
                <br>
                <label for="Contrasena">Contrasena</label>
                <input type="password" name="contrasena" placeholder="Ingrese su contrasena"/>
                <br>
                <label for="Nombre de usuario">Nombre de usuario</label>
                <input type="text" name="nom_usuario" placeholder="Ingrese su nombre de usuario"/>  
                <br>
                <button type="submit">Registrarse</button>
            </form>    
        </body>
        </html>
        """
    
    @cherrypy.expose
    def links(self):
        return"""
        <div align="center">
        </div>
        <h1 align="center">===================================================================================================== </h1>
        <h1 align="center"> FORO </h1>
        <div align="center">
        </div>
        <div align="center">
        <img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green">
        </div>
        <div align="center">
        </div>
        <h1 align="center">===================================================================================================== </h1>
        <ul>
        <div align="center">
        <img src="data:image/jpeg;base64,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" />
        </div>    
            <li><a href='/'>Home</a></li>
            <li><a href='/publicar'>Publicar</a></li>
            <li><a href='/information'>Information</a></li>
            <li><a href='/contact'>Contact</a></li>
            <li><a href="https://www.icci-unap.cl/">Ir a Icci UNAP
            
        """ 

    @cherrypy.expose
    def contact(self):
        return"""
        <div align="center">
        </div>
        <h1 align="center">===================================================================================================== </h1>
        <h1 align="center"> CONTACTOS </h1>
        <div align="center">
        </div>
        <h1 align="center">===================================================================================================== </h1>
        <ul>
        <div align="center">
        <img src="data:image/jpeg;base64,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" />
        </div>
        """ 
    @cherrypy.expose
    def publicar(self,nombre,apellido,email,contrasena,nom_usuario):
        return"""
        <div align="center">
        </div>
        <h1 align="center">===================================================================================================== </h1>
        <h1 align="center"> PUBLICAR </h1>
        <div align="center">
        </div>
        <h1 align="center">===================================================================================================== </h1>
        <ul>
        <div align="center">
        <img src="data:image/jpeg;base64,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" />
        </div>
        </html>
        </body>
            <form action="/formulario" method="POST">
                <h2>Registrarse</h2>
                <label for="anho">Anho de carrera</label>
                <input type="number" name="anho" placeholder="Ingrese el anho de su carrera"/>
                <br>
                <h3>Selecione el tipo de publicacion</h3>
                <label for="Pregunta">Pregunta</label>
                <input type="radio" name="Pregunta"/>
                <br>
                <label for="Aviso">Aviso</label>
                <input type="radio" name="Aviso"/>
                <br>
                <label for="Foto">Ingrese una imagen</label>
                <input type="file" name="Foto"/>
                <br>
                <label for="descripcion">Ingrese una descripcion</label><br>
                <textarea cols="100" rows="10" id="descripcion" placeholder="Ingrese descripcion de la publicacion" name="descripcion"></textarea>
                <br>
                <button type="submit">Publicar</button>
            </form>
        </body>
        </html>
        """
    
    @cherrypy.expose
    def publicacion(self,nombre,apellido,email,contrasena,nom_usuario):
        
        server= 'localhost'
        bd = 'FRAMEWORK'
        usuario = 'Benja'
        contrasena= 'server'

        try:
            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+';DATABASE='+bd+';UID='+usuario+';PWD='+contrasena)

            print('conexion exitosa')

        except :

            print('error al conectarse')    


        # Consulta a la BD

        cursor = conexion.cursor()
        cursor.execute("Select * from usuarios;")

        # usuarios = cursor.fetchone()

        # while usuarios:
        #     print(usuarios)
        #     usuario = cursor.fetchone()

        #=============================================
        usuarios = cursor.fetchall()

        for usuario in usuarios:
            print(usuario)

        #############################################

        # Insertar datos en la tabla

        cursorInsert = conexion.cursor()

        consulta = "Insert into usuarios(nombre, apellido, email, contrasena, nom_usuario) values ('{}','{}','{}','{}','{}')".format(nombre,apellido,email,contrasena,nom_usuario)

        ###cursorInsert.execute(consulta,nombre,apellido,email,contrasena,nom_usuario)

        cursorInsert.execute(consulta)

        cursorInsert.commit()
        cursor.close()
        conexion.close()
        
        return
    @cherrypy.expose
    def information(self):
        return"""
        <div align="center">
        </div>
        <h1 align="center">===================================================================================================== </h1>
        <h1 align="center"> INFORMACION </h1>
        <div align="center">
        </div>
        <h1 align="center">===================================================================================================== </h1>
        <ul>
        <div align="center">
        <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgTERUTExASFRIXGBcXGBgYFhcXGRsbGBUWFhkeHx4bHSghGCYxIBkfITEhJikrLi8uICszODMwNzAwMDABCgoKDg0OGxAQGzAmICYvMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwLzAvMP/AABEIAMgAyAMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAAAAQYHAgQFAwj/xABEEAACAQIEAgcGAwUFBwUAAAABAgADEQQFEiEGMQcTQVFhcZEUIjJSgaEjQsEzNHKxshWCouHwFmKDk8LD0hckRUZU/8QAGgEBAAMBAQEAAAAAAAAAAAAAAAEDBAIFBv/EADoRAAEDAQMJBwMDAgcAAAAAAAEAAhEDBCExEhRBUWFxgbHRBRMiUpHB8DKh4TOy8RVyIzRCQ2KCwv/aAAwDAQACEQMRAD8A0IRQntL4FOEUIROEUIROEUIROEUIROEUIROEUIROEUIROEUIROEUIROEUIROEUIROEUIRYwihOlKcIoQicIoQicIoQicIoQicIoQicIoQicIoQicIoQicIoQicIoQicIoQicIoQixvC8xvLJ/wDTKj/+tv8Alj/ynNSq2nGUVqoWWrXnuxMY3gY7zsVcXhebudYEUK9SiG1BGte1r/SaF52LxIVLmFpLTiFleF5jeF5MKIWV4XnayThjM8VvTQCn87Gy/TtP0Ek9DozP58UL9y07/ct+kpfXptMErVSsNeqMpjbuA5kKvrwvJ9iOjSoB+HiVJ7ihX7gn+Uiec5HmGFa1WmQDyYbg+R/TnJZWY8w0rmrY61IS9sDXceRXNvC8xvC8thZ4WV4Xm7leU4/ENpo02Y9p5KPMnYSXYTo1xJH4mJVT3BS/3JEqfVYz6itFGyVqwmm2R80m5QS8Lywq3Rl8mL37mp/qG/SRrOuE82wwLMgemObqdQHntceZFpDa9NxgFdVLBaKYlzLuB5ErhXheY3heXQskLK8LzG87+S8KZriQGVAtM/nY6QfLtP0Fpy5waJcVZTpPqOyWCSuFeF5YVDoy29/Fb9y0/wBS36TwxXRriQL08SrHuKlfuCZTnNKcea1/0y1ROR9x1UEvC83c0yjH4dtNamy9x5qfIjYzQvLxBEhYnNLTDhBWV45heEmFEJGfRM+dbz6KmG3/AOnj7L3uxf8Ac/6/+lSHGn79iP4v0E4s7XGn79iP4j/ITiXm2n9A3DkvIr/qv3nmU5JuB8gXFViXB6mnYt/vE8h9t/ASMXlu9GuGC4FWtu7M3odP/TKrTULKcjctHZ9BtauA7AX+ilFNEUAAAKBYAbAAfynAx/GmRUmKmqWI56VLD15H6GcvpPzarSopSQkdbq1Edy22+pP2lW3mSz2UPblOK9S3douov7umBIxJV2ZXxVk1dtCVrOeSsCpPlfY+QM6uNwtCqjU6ihkYWIP+tvOfPwJlzcCZpVxGFBc3dGKMe02sQT9CPSRaLMKYDmldWG3m0E06gExwPC/8qseJsnfCYhqZN1+JD3g3t/K3mJ7cKZBVxlbTcrTWxdu4dgHif85LOljCjRQq25MyH+8NQ/pPrO/wTlq0MHT299xrbzbcD6CwlzrQRQDtJuWNnZ7Ta3MP0i/gcB6/YLr4DBYeigp00CoOQH8z3nxnIzTi/JaDFWq6nHMKC1vM8vpecDpG4jqU7YakxDEXqMNiAeQ8L8z4W7zK1vKqFlyxlPWm2dpdy7u6QF2nQNgCt7DdIGRMbFnTxZdvsTJLQrUaihkZWRhsRYgifPl5I+DeJKuFrAMxNByAy9gvsCO4jt7x9J3VsQyZYqrP2s4viqBGsTdvvw5LucecKIgOIoLZfzqOQv2juHeOzykBn0JVpU3UqwBVgQR2EEWMpU5I39oeyb/tNN+21739N53ZK2U0h2jkq+07GGPa6mPqMRt/KkfAfCdNwMTXW63/AA0PJrfmPeO4dvlzsWvVpIpZmVVA3JIAA8+yOhSpoqqosqgADuAFhKg404jqYqsVVj1CEhAORttc99+zuH1mYB1oqSbhyC3vdTsFEACSfudJ3DoFOsTx/kSmwd38VXb7kTZyvjDJa7BVq6WOwDArf68vpeUveF5qNipxiV5o7XrzeB6HqV9AY3B4eshp1EDIeYP+tj4iU7xbkD4Stp3NJrlG8O0HxElfRzxHUf8A9tVa5AvTJ52HNfGw3Hhfwki40y1a+DqL+ZRrXzXc+ouPrM1MuoVMk4fL16Fopsttn7xn1DDho6eqpWEV4T1V80kZ9Fz50n0FgK4qUqdT51VvVQf1mC34N4+y9zsU31B/b7qmONlIx+I/iv6gGcWSbpIwlRMa7Ee7UCsp8lCn7j7yMTZSMsadgXl2luTWeDrPNOXZwQtsBQ/hY+rsZSIvL54fwr0sNRpsLMqKGHcbXI9Zltx8AG1ej2O3/Ecdnv8AhQPpYYddRHboP3b/ACkEkx6VKynFqo/LTUHzLMf5WkNl9m/SasdvvtL9/sE5Z/RO34FUdmsH1X/KVfLO6Jf2Nb+Jf6ZxbP0jwVvZf+ZG48ludKCg4LyqKf8ACw/WS5EUAAcgLD6SJdKP7l/xF/ped7IcatbDUqoN9Si/8QFmHqDPOcJotO0+y91hGcvH/FvN3VU9xfVdsdiCeeth9FOkfYCciS3pJyhqWJNYD3K29+wEABh+v18JEZ69JwcwEal8zamFlZwdrP3MpxQmzluCrV6qUkF2cgDw7yfADeWTF5VGSXXBXhkNRmw1Bje5ppe/8I3/AFkQNNf9oOX5b/X2e0nOEw1OnTSmvwoqqPJQAP5SFf8Az/8Ad/7E8agb3/2lfU2tt1IHzt91Lc7dlw1dhzFKoR5hGIlCCfQmJoI6MjfCylT5EWMoTM8DWoVXpOLMhIPj3HyI3mmwEeILD2y0ksdovHFa8IoT0F4a6/CVR1xtArz6xR9GOk/YmXk6ggg8jtKk6NsoariRVI9yjvfvJBCj9fpLMzrGrQw9WoTbSpI8zso9SBPLtpyqgaPkr6PslpZQLnYTPoFQ0UIp6hxXzYwRLX6Nc7Srh+oY/iUuQ71vsfpy9JU098Hi61J1qU2KupuCP9faV16IqsyVtsloNCplaMDuV5Z9keCxVPRVHLdWGzKfA/pINX6McVf3MShX/eVgftebeTdJOHIC4mmyt867qfErzH0vJAnG3DZF/aQPNKg/6Z5zc4o3AHmF7T8ytPicRO+CtDh3gTCYdhVqN1tQbqLWVT323ufH7SU4zFUaSNUqMFRRcmRnG9IORIPcZ6p7lRh92t+sr/iXirG4s2ayUgbhAdvMn8xgUK1Z01JG/wBlDrVZ7NTilBOoX+pXPzvMXxGIqVjtra4HcBso+gAE0pjCesAAIC+ecS4knErKWf0S/sa38S/0yrpP+jnPMsw9KotaqELMCAQxuNNuwGZ7W0mkQNi29nODa4LjAgrvdKP7l/xF/peR/o14gRGOFqGyOb0yeQJ2K/X+fnNvj/iHKa+ECUqwd9amwDDYBr8x4yt7yqz0cqhkPuvV9stPd2oVKZm4e8hfQOZ5dhcRTNKqoZD6g9hB7DK4zbo5zBWJoOtROwMdJH6HzuPKLhrpBr0wKeJDVFGwcH3gPG/xfY+cnOC4pyKqLriafkx0H/FaZor2fDDdIW4my2wCcfQ/keoVd4Lo9zxjZ1SmO0syt9heT/hjhfBYRbj36pFmci23cB+UTdr59lCD3sTR8g6k+gN5Fs86RsIgK4desb5mBVR9Pib7QX16/hi7dA9UbRsll8ZN+0yeA/CnsgP/ANg/uf8AYkhyTOcM+HpNUxFLrGRS12UHURvtfbykaoVqT59qRlZdHNSCP2HeJxRaQXg+Uq21ODhSI87VYUj3E3DGCxgBa6VQLK45+RH5hOjnFV0w9Z1NmSm7Kediqkj7iRLI+kfCMAuIXq3+ZQWU/T4l+84pMqHx09GrFWWipR/Tq4HXh66FHMZ0fZ4hsipUHYVZV+xtabeU9HGYMwNd0pp2hffJ/Qed/pLAw+f5Q4uuJo+RdQfQm88MZxTkdIXbE0/JTrP+G8vzqufCBfu+clk/p9kb4ybtpu+cVv5Xl2FoUxSpLpQepPaSe0yu+kriJKjDC0muqG9QjkWHJfp2+PlMOJOkGvUBp4ZWpqdi5+I+Vvh8+flILeXWayuDsupj8vWa3W5jmd1Sw0n2Gz5uyhMYT0F46ITGElSsoTGEIsoTGEJKyhMYRCiQsoooQkhOOYwhJWUUUIUpwihJUXJyRcBYvD0sbTeo6ogDXZjYb0yBI5CcPZltLTpXdKp3bw8aDKuvO+IMnbDV1XE0izUqgADi5JRgAJSsUJVQs4pAgGZWi1Ws2ggkAQnCKE0LJcsoTGEhSsoTGEIlCKE6hTC7+Gw1M5bVfQC61qY1aRqClWuL8wL2kw/s3Kr4mnVpogYYZFYKoNNnpXvy23tfv7ZAMpzvMcMWNGqU1W1CysDblswI+swxGbY9xUD1WYVWDPe3vFb6T4WvyEzPpOcTfdxnRyj5p3U7RTY0XSYjZg7TtytWj0nua4DD4dHvQpF6WEwzEaVILitpYnbcm1ie0TwzXLMDQWviRTRkrmkuHBVSFFQBqhA5LYXAI5SH4rP81qatdZm1KqNcDdVbUBy7ze/OeFfNca6U6bVCUpX0Db3b/wA/rOWUHiJO/HYeYjirKtrpumBouwxvHI+oCsXNUy4Y2nQVMHbrqQNNaFnANibtbSR4eMea4TLVqYcvhqTlq1QgYekbGmisCGA2YhrEjuBkfx+M4sI97Eq5plXKq1MsnIqxW17e8O+195rVXz+mWUYhC1JnrMFZSUZTpY8tt2tYbHeUNpXDxDDWd2gDWFpdaMfAcRoGvDGDgemK79fCUXLVdOGqUmwmJKVEpaLslt2Q/ARewI3nqaeEfF08EcJQ6p6KszqgV1Jplr6h498itHNM9xJqO2IUBKbKxbSihHZUYWC2FyQNheb1fE8RNh7NjU6ohlC60UuqWVtNgLjste5sdjOjSIuJGrdqwGPpwXLbQCJDTrwF40i8kgHDEneV2Ms4XRsv0GkrVaivUV/d1KVKmkBfezAE7d88KD4dFwNH2OhVFZbOTTGvd9JII3FhvecSrhs66+g4xCNXYIKRVl2WzAG1rAAA7zYw+P4nAq0va1prSbq21MiAMxY2Btt8DG94LCZJcDp03YjbhdqwXLagbADSLgNBkCD9xOvGdgeRZDQOZ1KenXRos7EG1mCsQqm+xubDfnvO9SyTDJj2Y0aSpUwzVFRlVqdNgFDDa42O+3YdpEsLlubotZGqJQpswWoXYAOR74ANiW2INxtYjvmWFOfI/soqhdFOra5QqKbr1jENY3UgXuJ29pcTDxhHDGdUzzVdJ7WAA0zjPHAD00ngNKk9T2OnmNCgcPhmaoqCtakNF/eINMNy2O5HOcrNHo1cHin6igj0qqKClNUsuptzbv5X7bCaRoZ4GpMa6Woprp1NSFQodUsDY3szAaTyvPDIq2cpWqmhiEXbVVqEr1dtWxOoEHc7WF99oFMDxSJEadu6667XohdPqky0gw4nQNI36DJxAU1wOWULOFpYZamjCAdbTUqGdTq2te5PqZzMyTL8OuJxNHDo7CsKQDJdaY0LqYKeV2uBf/KR3Mamc6aztiVqIzUmqMrq2pvf6vkLrbSdtrWG3KbtN+KFqPWFYB2W7n3DqVaArbqVsx0EcxfsnHdReXD1Iwi74LhvXZrz4Qw7LgYkuggT/MHCL9fiilQahhcSKSUalYPrRBpU6GAVgvZcH6yZZrQyVa4psuF1GtQFJKdMBxd01h7CxBUnY98geMXMsSoxFeuhuWVdTBSdIUkKoFh8Q2HfOdVzPGNW69nJralbVYX1Laxta3YJb3JcAJwnXsgcFQLSKZLsn6snVgBBN2kzMYSp7xZlWGZFRadAVamIKUTRTQAAxRlcgWJB5+R7Lw4ty2nh0p4ijh6VqDGkwZVZaisoCuwB3Oq433vYyGUOJM2UkrWIJc1Dsp95rgsLjY7nlNSjmGLVKiK50VbaxsdVjcXv49shtB4iTcN983H7b9Kmpa6bsogGTp1Rhvv3XRipF0gVqS1zRSjRpqoVroioxLKCbkcxvIpPfHY7E1n11GLPYC+w2AsOXhNeaKTMhgasdep3lQu+QnCKEshUwlFCEldIhCEIiEcz9nr/ACN6GSoUmrZ1lgqVKyGq1WoqppZUVVGhUY3DEtspsLDnPbF57llSrVc1auiotRbDD0lKa3Vh8NT8Tla5I+5kT9nr/I3oYez1/kb0Mo7hvz+Fqzp2oa9O3bt6RdHbyfMMBRNdOsqaaiqqv1KMRZ1Y3ps+n8pHxHvm5RzrL1oshqValxU/Dekmlma+hlsx6kgkEgXvbnIx7PX+RvQw9nr/ACN6GSaLSZPtu1KG2lzRAA++udevXxlSKhn2DTS/VlqiYcUVDbLqZmDElWDAaGIFt7nsnpic4ymurdZ1lJnNBn0KrjVSWqhtqcGxVlNzc3B85GfZ6/yN6GHs9b5G9DHctF4n5+Uzl2BAjVwjRBwuxUkx+c5bilFOr1lJaZ/CZVWodOimlmBZbm1MHVftM8hneDOJLkOtDqGoLsrsAaJpBiLqCbm5Fx3Tgez1/kb0MPZ63yN6GO5aBAwiN0qDaXE5RiZBnXGE6PQBSnCZ5ltOn1CPVCBGAqGklRizVKLkmmzWAtSt8R3N5zsJmGBvXp1Hc0q2k61VFZWVtSnqw2m25BUHynH9nr/I3oYez1/kb0MkUmidvz5o2I60ExcLt+GrH747V3qWb4TD0qqYZ6hZzSOtkSx0dZq90ltPxrbmdjuJ0anFGActq6wagwYhEJGrBpQJA1AHcE2uNvSRD2et8jehh7PX+RvQzk0GG8/PkKW2p7bhEar409SpCMyy4YbqFr1QA1U3OGpNqDogtvUvTsVO6k8wfCRqens9b5G9DD2ev8jehljWhsqqpUL42b/eV5wjinS4RHFCETihCERCKElSnCKKEVr9FeVYQYc4gqDVZ2UMfygW2Hd4mdTG5xmSvWcVKApUqjUurcEM1sMK1w192ufhtyBlc8JcX4rB6l0CpSY3KE6bHlcGxt6dk7dTj3J2q9cctBq8tRdSeWn5d9tr908ivZarqhdEjRh6XwvdstsospNbMEb/AGC71LPM5NRcP1tLW7UCKop/CKtGrUI06rHensb8jDDcR5owSoTSCqcMroEPvms5RiDq921rgWM4GE44yWnbq8tC6W1CzjY6St/h7iRMV43yQMj/ANmjVTtoOsXFiSPy9hJI7pVmdXy8uqvz+j5/3dFIsPn2bacO7VcOwrthzoC2dFq1tDC1zcWNtXfPLC59nhCVGq0yhTDVSopW2xGI6nRfV2AXv2zg0eNsjQkrliqSyvs4HvI2pT8O1jvaey8fZSAAMu2C01A6wfDTbWg+HsbcRmdXycuqZ/R8/PouxlvEebVHFz7opdYwWkCP2lYWZtQKCyAXAMK+eZ2tKoeup6lpYeuCKXZWJUpYt2cwec4H+2eRXDf2YLqLD8TkLk2+HvJ9Z7tx9lJBBy7YqiEdYN1Q3QfD2GMzq+Tl1TPqPn59FJ6WbZqMRpapTamtdMOR1ektqo9YXvq2N+zlaetDOMxOL9mKnUKzs3uG3s+g9W2rlu23O9wRImePsqNbrzlw6359Yvy0/LzttfumwOkrBdYansR6wqELdYL6QSwHw95JkZnW8v3HVM/o+fn0XYzHNM6ptirV1YUWw6qBRFz19RB825AJHj4TXq8SZwmIWmSSL0AQ1EL+1NS+ohiKZsosLm85GJ6QMrqCoHy/V1mnXeoPe0WK393stPGnxxkqiwy3a6H9p202LJ+XsLE/WTmdXycuqZ9R8/7ui7OScTZtV0qzKGc0PeNLSR1qVibC/vqCgIbbtE2MPm+dsEXr6eqpUxK6uqHujD6xy1b6rDytOHT49ylShGXWKBAv4g2CatP5ezUfWYV+OsmdNDZaCmpnsXHxMSWPw9tzGZ1fJy6pn1Hz8+i6y8W5oXv7oVqam3V+6CcCMTs99zqNtNuU6WXZ5mL1UJNPqmr+zlNO/wC7Ctr1X79rW5SNNx7lBBBy7YkG2sWuKfUj8vye75TGnx5k61RVXLrVQLBtYv8ADp+Xu2v3RmdXycuqZ/R8/wC7ouv0qZXhDhxiAoFVXVSw/MDfY9/gZVUkfFvF+KxulSgp0lNwgOq5ta5Nhfw27ZG56dlpvp08l+K8W21WVKpczDmnCKE0rKnCKEIlCKElSnCKEInFCEInCKEInCKEInCKEInCKEInCKEInCKEInFCEInCKEInCKEInCKEIlCKE6UpwihCJwihCJwihCJwihCJwihCJwihCJwihCJwihCJwihCJwihCJwihCJwihCIhCEhEQhCERCEIREIQhEQhCERCEIREIQhEQhCERCEIREIQhEQhCERCEIREIQhF//Z" />
        </div>
        """

    @cherrypy.expose
    def Validar(self,nombre,apellido,email,contrasena,nom_usuario):
        
        server= 'localhost'
        bd = 'FRAMEWORK'
        usuario = 'Benja'
        contrasena= 'server'

        try:
            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+';DATABASE='+bd+';UID='+usuario+';PWD='+contrasena)

            print('conexion exitosa')

        except :

            print('error al conectarse')    


        # Consulta a la BD

        cursor = conexion.cursor()
        cursor.execute("Select * from usuarios;")

        # usuarios = cursor.fetchone()

        # while usuarios:
        #     print(usuarios)
        #     usuario = cursor.fetchone()

        #=============================================
        usuarios = cursor.fetchall()

        for usuario in usuarios:
            print(usuario)

        #############################################

        # Insertar datos en la tabla

        cursorInsert = conexion.cursor()

        consulta = "Insert into usuarios(nombre, apellido, email, contrasena, nom_usuario) values ('{}','{}','{}','{}','{}')".format(nombre,apellido,email,contrasena,nom_usuario)

        ###cursorInsert.execute(consulta,nombre,apellido,email,contrasena,nom_usuario)

        cursorInsert.execute(consulta)

        cursorInsert.commit()
        cursor.close()
        conexion.close()
        
        if nombre == "":
           ValidarN="Ingrese un nombre valido"
        else:
            ValidarN=nombre

        if apellido == "":
           ValidarA="Ingrese un apellido valido"
        else:
            ValidarA=apellido

        if email == "":
           ValidarE="Ingrese un Email valido"
        else:
            ValidarE=email

        if contrasena == "":
           ValidarC="Ingrese una contrasena valido"
        else:
            ValidarC="Contrasena valida"

        if nom_usuario == "":
           ValidarNo="Ingrese un nombre de usuario valido"
        else:
            ValidarNo=nom_usuario   
             
                
        return "Bienvenido"+ValidarN+" "+ValidarA+"Tu email es: "+ ValidarE+ " y  "+ValidarNo
                
cherrypy.quickstart(Home())         