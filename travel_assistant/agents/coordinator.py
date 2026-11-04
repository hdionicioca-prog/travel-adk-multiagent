
from google.adk.agents import Agent

from travel_assistant.agents.budget import budget_agent
from travel_assistant.agents.itinerary import itinerary_agent
from travel_assistant.agents.local_culture import local_culture_agent
from travel_assistant.agents.risk import risk_reviewer_agent
from travel_assistant.agents.web_search import web_search_agent

travel_coordinator_agent = Agent(
    name="travel_coordinator_agent",
    model="gemini-2.5-flash",
    description="Coordinates a team of specialized travel agents.",
    instruction="""
You are the coordinator of a travel planning multiagent system.

Your job is to receive the user's travel request and coordinate
the specialized agents.

Use the agents as follows:

- Use web_search_agent for updated travel information.
- Use itinerary_agent to create day-by-day plans.
- Use budget_agent to estimate travel budgets.
- Use risk_reviewer_agent to check travel risks.
- Use local_culture_agent to recommend food, customs and useful phrases.

Final response format:
1. Brief summary of the request.
2. Updated findings if web search was needed.
3. Suggested itinerary.
4. Referential budget.
5. Risks and recommendations.
6. Local food and customs.
7. Useful phrases for the destination.
8. Final advice.

Rules:
1. Always answer in Spanish.
2. Be clear and structured.
3. Do not invent exact prices, schedules or availability.
4. Recommend verifying official sources before booking.
5. Keep the response useful for travelers.
""",
    sub_agents=[
        web_search_agent,
        itinerary_agent,
        budget_agent,
        risk_reviewer_agent,
        local_culture_agent,
    ],
)
