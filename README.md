
# Travel ADK Multiagent

Sistema multiagente de planificación de viajes desarrollado con Google ADK.

## Descripción

El proyecto utiliza agentes especializados para ayudar al usuario
a organizar viajes, consultar información, estimar presupuestos
y conocer los riesgos y costumbres de un destino.

## Agentes

- Travel Coordinator Agent
- Web Search Agent
- Itinerary Agent
- Budget Agent
- Risk Reviewer Agent
- Local Culture Agent

## Tecnologías

- Python
- Google ADK
- Gemini
- Poetry
- Pytest
- Ruff
- Git y GitHub
- GitHub Actions
- SonarCloud

## Instalación

```bash
poetry install
```

## Configuración

Crear un archivo `.env` y agregar:

```env
GOOGLE_API_KEY="TU_API_KEY"
```

## Ejecutar por consola

```bash
poetry run adk run travel_assistant
```

## Ejecutar interfaz web

```bash
poetry run adk web --port 8000
```

## Ejecutar pruebas

```bash
poetry run pytest
```

## Análisis de código

```bash
poetry run ruff check .
```
