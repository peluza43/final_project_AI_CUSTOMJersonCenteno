# Gestor de Conocimiento con CAG

Proyecto final — Inteligencia Artificial  
Universidad Mariano Gálvez de Guatemala  
Estudiante: Jerson Centeno

---

## ¿Qué es este proyecto?

Sistema de preguntas y respuestas con dos capas de inteligencia:

- **RAG** (Retrieval Augmented Generation): recupera información de una base
  documental para responder preguntas.
- **CAG** (Context-Augmented Generation): guarda el contexto del usuario
  (preferencias, historial) y lo usa para enriquecer respuestas futuras.

---

## Arquitectura
frontend/          → Interfaz web (HTML + CSS + JS)

backend/

server.py        → Servidor HTTP (rutas /health, /api/ask, /api/context)

assistant.py     → Orquestador RAG + CAG

knowledge.py     → Recuperación documental (RAG)

context_store.py → Almacenamiento de contexto por usuario (CAG)

cag.py           → Aplicación de contexto a la respuesta (CAG)

data/

knowledge_base.json → Base documental del curso

tests/

base/            → Pruebas del sistema RAG base

validation/      → Pruebas del contrato CAG

docs/

evidencias/      → Capturas del proceso de desarrollo
---

## Flujo RAG + CAG
POST /api/ask

↓

retrieve_snippets(question)     ← RAG: busca en knowledge_base.json

↓

context_store.list_for_user()   ← CAG: recupera contexto del usuario

↓

apply_context()                 ← CAG: enriquece la respuesta

↓

Retorna answer + sources + context_used
---

## Instalación y ejecución

```bash
# Instalar dependencias
pip install pytest

# Correr el servidor
python -m backend.server

# Correr todas las pruebas
python -m pytest tests/ -v
```

---

## Pruebas

```bash
# Pruebas base (RAG)
python -m pytest tests/base/ -v

# Pruebas CAG
python -m pytest tests/validation/ -v
```

Resultado final: **6/6 pruebas pasan**

---

## Scrum

### Backlog

| ID | Historia | Prioridad |
|----|----------|-----------|
| US-01 | Guardar contexto por usuario | Alta |
| US-02 | Recuperar contexto por usuario | Alta |
| US-03 | Aplicar contexto a la respuesta | Alta |
| US-04 | Documentar proceso con PROMPTS.md | Media |
| US-05 | Actualizar README y evidencias | Media |

### Sprint 1 — Implementación CAG
**Duración:** 12/06/2026  
**Objetivo:** Implementar los tres módulos CAG y pasar las 6 pruebas.

| Tarea | Estado |
|-------|--------|
| Analizar arquitectura base | ✅ |
| Implementar ContextStore | ✅ |
| Implementar apply_context | ✅ |
| Conectar assistant.py con context_store | ✅ |
| Verificar 6/6 pruebas | ✅ |

### Sprint 2 — Documentación y cierre
**Duración:** 12/06/2026  
**Objetivo:** Completar documentación, evidencias y Pull Request.

| Tarea | Estado |
|-------|--------|
| Subir evidencias a docs/ | ✅ |
| Actualizar README.md | ✅ |
| Completar PROMPTS.md | ✅ |
| Crear Pull Request | 🔄 |

---

## Uso de IA

Ver `PROMPTS.md` para el registro cronológico completo del uso de IA
durante el desarrollo, incluyendo prompts, decisiones humanas y verificaciones.
