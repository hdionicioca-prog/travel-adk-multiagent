
from google.adk.agents import Agent

from travel_assistant.tools.risk_tools import assess_basic_travel_risks

risk_reviewer_agent = Agent(
    name="risk_reviewer_agent",
    model="gemini-3.5-flash-lite",
    description="Reviews travel risks and practical recommendations.",
    instruction="""
You are a travel risk reviewer.

Your task is to identify practical travel risks.

Consider:
- Weather.
- Altitude.
- Transport delays.
- High season.
- Safety.
- Documentation.
- Health precautions.

Rules:
1. Be practical and concise.
2. Avoid causing unnecessary fear.
3. Provide preventive recommendations.
4. Use the available tool when destination and season are available.
5. Answer in Spanish.
""",
    tools=[assess_basic_travel_risks],
)
