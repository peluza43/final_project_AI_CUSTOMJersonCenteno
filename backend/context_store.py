"""Base placeholder for student implementation."""


class ContextStore:
    def save(self, user_id, key, value):
        raise NotImplementedError("CAG context storage is not implemented yet")

    def list_for_user(self, user_id):
        raise NotImplementedError("CAG context retrieval is not implemented yet")
