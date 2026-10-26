class NavegadorController:
    def __init__(self):
        # Pila para almacenar las páginas visitadas (LIFO)
        self.pila_historial = []

    def visitar_pagina(self, url: str):
        """Registra una nueva página en la pila."""
        url = url.strip()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        self.pila_historial.append(url)

    def regresar_pagina(self):
        """Regresa a la página anterior eliminando la actual (pop)."""
        if not self.esta_vacio():
            return self.pila_historial.pop()
        return None

    def obtener_pagina_actual(self):
        """Devuelve la página actual sin eliminarla (peek)."""
        if not self.esta_vacio():
            return self.pila_historial[-1]
        return None

    def obtener_historial_descendente(self):
        """Devuelve el historial en orden descendente (de la más reciente a la primera)."""
        return list(reversed(self.pila_historial))

    def esta_vacio(self) -> bool:
        """Verifica si el historial está vacío."""
        return len(self.pila_historial) == 0

    def limpiar_historial(self):
        """Vacía completamente la pila de historial."""
        self.pila_historial.clear()