import web
from controllers.navegador import NavegadorController

# Definición de rutas del sistema
urls = (
    '/', 'Index',
    '/action', 'Action'
)

# Renderizador de plantillas apuntando a la carpeta 'views/'
render = web.template.render('views/')

# Instancia global del controlador
navegador = NavegadorController()

class Index:
    def GET(self):
        return render.index(
            pagina_actual=navegador.obtener_pagina_actual(),
            historial=navegador.obtener_historial_descendente(),
            esta_vacio=navegador.esta_vacio()
        )

class Action:
    def POST(self):
        user_data = web.input(accion=None, url="")
        accion = user_data.accion

        if accion == 'visitar':
            url = user_data.url
            if url:
                navegador.visitar_pagina(url)

        elif accion == 'regresar':
            navegador.regresar_pagina()

        elif accion == 'limpiar':
            navegador.limpiar_historial()

        # Redireccionar a la vista principal
        raise web.seeother('/')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()