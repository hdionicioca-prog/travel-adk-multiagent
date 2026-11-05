# Travel ADK Multiagent

Sistema multiagente de planificación de viajes desarrollado con Google Agent Development Kit (ADK).

## Descripción

El proyecto utiliza agentes inteligentes especializados que colaboran para ayudar al usuario a planificar viajes. El sistema permite consultar información de destinos, generar itinerarios, estimar presupuestos y evaluar riesgos, además de proporcionar recomendaciones culturales.

## Arquitectura del sistema

El sistema está compuesto por un agente coordinador y cinco agentes especializados:

- **Travel Coordinator Agent:** recibe las solicitudes del usuario y coordina el trabajo de los demás agentes.
- **Web Search Agent:** busca información actualizada sobre destinos y viajes mediante Google Search.
- **Itinerary Agent:** propone itinerarios organizados según la duración y características del viaje.
- **Budget Agent:** estima los gastos aproximados del viaje.
- **Risk Reviewer Agent:** identifica posibles riesgos y ofrece recomendaciones preventivas.
- **Local Culture Agent:** proporciona información sobre gastronomía, costumbres y expresiones locales.

## Tecnologías utilizadas

- Python 3.14
- Google ADK
- Gemini
- Poetry
- Pytest y Pytest-Cov
- Ruff
- Git y GitHub
- GitHub Actions
- SonarCloud

## Requisitos previos

- Python 3.14
- Poetry
- Una clave API de Google AI Studio

## Instalación

Clonar el repositorio e ingresar a la carpeta del proyecto:

```bash
git clone https://github.com/hdionicioca-prog/travel-adk-multiagent.git
cd travel-adk-multiagent
```

Instalar las dependencias:

```bash
poetry install
```

## Configuración

Crear un archivo `.env` en la raíz del proyecto y agregar la siguiente variable:

```env
GOOGLE_API_KEY="TU_API_KEY"
```

Reemplazar `TU_API_KEY` por una clave válida de Google AI Studio.

## Ejecución del sistema

Para ejecutar el agente desde la consola:

```bash
poetry run adk run travel_assistant
```

Para iniciar la interfaz web:

```bash
poetry run adk web --port 8000
```

## Pruebas y calidad del código

Ejecutar las pruebas unitarias:

```bash
poetry run pytest
```

Ejecutar las pruebas con cobertura:

```bash
poetry run pytest --cov=travel_assistant --cov-report=term-missing --cov-report=xml
```

Analizar la calidad del código con Ruff:

```bash
poetry run ruff check .
```

## Integración continua

El proyecto utiliza GitHub Actions para automatizar la instalación de dependencias, el análisis estático con Ruff, las pruebas unitarias con Pytest y el análisis de calidad mediante SonarCloud.

El flujo se ejecuta automáticamente al realizar cambios en las ramas `develop` y `main`, así como al crear Pull Requests hacia ellas.