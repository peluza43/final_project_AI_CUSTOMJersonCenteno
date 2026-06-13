"""Implementacion CAG: almacenamiento de contexto por usuario en memoria."""


class ContextStore:
    def __init__(self):
        self._store = {}

    def save(self, user_id, key, value):
        if user_id not in self._store:
            self._store[user_id] = []

        # Actualizar si la clave ya existe
        for item in self._store[user_id]:
            if item["key"] == key:
                item["value"] = value
                return True

        self._store[user_id].append({"key": key, "value": value})
        return True

    def list_for_user(self, user_id):
        return self._store.get(user_id, [])