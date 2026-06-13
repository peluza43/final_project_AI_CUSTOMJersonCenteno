## Entrada 1 — Análisis de arquitectura base

**Fecha:** 12/06/2026
**Sprint:** Sprint 1 — Análisis y planificación

**Objetivo del prompt:**
Analizar el proyecto base sin generar código, identificar la arquitectura RAG existente
y los puntos exactos donde debe integrarse el módulo CAG.

**Prompt usado:**
"Analiza este proyecto Python y NO programes todavía. Explica la arquitectura actual,
el flujo RAG, dónde integrar el contexto CAG, cómo afecta el flujo, y propón
arquitectura de bajo acoplamiento."

**Resumen de la respuesta:**
Claude identificó 5 archivos clave, describió el flujo RAG actual (server → assistant →
knowledge), y señaló que context_store.py y cag.py son stubs vacíos con NotImplementedError.
Identificó que assistant.py nunca llama a CAG y que context_used siempre retorna [].

**Decisión humana tomada:**
Implementar ContextStore con diccionario en memoria por simplicidad.
Modificar assistant.py para orquestar RAG + CAG.
apply_context() modificará la respuesta si existe contexto del usuario.

**Cambios realizados:**
Ninguno aún — esta entrada documenta solo la fase de análisis.

**Verificación aplicada:**
Pruebas base ejecutadas: PASAN.
Pruebas CAG ejecutadas: FALLAN (esperado, stubs sin implementar).
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
## Entrada 4 — Documentación final y cierre

**Fecha:** 12/06/2026
**Sprint:** Sprint 2

**Objetivo del prompt:**
Generar README.md completo con arquitectura, flujo CAG, Scrum y documentación final.

**Prompt usado:**
"Genera README.md con arquitectura del proyecto, flujo RAG+CAG, backlog Scrum,
sprints y resultados de pruebas."

**Resumen de la respuesta:**
Claude generó README completo con árbol de archivos, diagrama de flujo,
tabla de backlog, sprints y comandos de ejecución.

**Decisión humana tomada:**
Revisé y ajusté el contenido para que refleje exactamente mi implementación.

**Cambios realizados:**
README.md reemplazado con documentación completa.

**Verificación aplicada:**
Revisión manual del documento. Pruebas finales: 6/6 pasan.