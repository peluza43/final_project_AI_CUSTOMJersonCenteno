## Entrada 2 — Implementación ContextStore
**Fecha:** 12/06/2026
**Sprint:** Sprint 1

**Objetivo del prompt:**
Implementar context_store.py para guardar y recuperar contexto por usuario.

**Prompt usado:**
"Implementa ContextStore con save() y list_for_user() usando diccionario en memoria."

**Resumen de la respuesta:**
Claude generó implementación con diccionario _store, manejo de claves duplicadas
y retorno de lista vacía cuando el usuario no tiene contexto.

**Decisión humana tomada:**
Elegí almacenamiento en memoria por simplicidad. Es suficiente para el examen
y no requiere base de datos externa.

**Cambios realizados:**
context_store.py implementado completamente.

**Verificación aplicada:**
test_saves_context_for_user: PASS
test_retrieves_context_for_user: PASS

## Entrada 3 — Implementación CAG y conexión con assistant.py

**Fecha:** 12/06/2026
**Sprint:** Sprint 1

**Objetivo del prompt:**
Implementar apply_context() y conectar el flujo RAG+CAG en assistant.py.

**Prompt usado:**
"Implementa apply_context para que la respuesta incluya el contexto del usuario.
Corrige el problema de instancias separadas de ContextStore."

**Resumen de la respuesta:**
Claude identificó que el problema era dos instancias distintas de ContextStore.
La solución fue pasar context_store como parámetro a answer_question() desde server.py.

**Decisión humana tomada:**
Acepté pasar context_store como parámetro porque mantiene bajo acoplamiento.
apply_context agrega el contexto al final de la respuesta en formato legible.

**Cambios realizados:**
cag.py implementado. assistant.py modificado para recibir context_store.
server.py modificado para pasar su instancia compartida.

**Verificación aplicada:**
6/6 pruebas pasan: 3 base + 3 CAG.
