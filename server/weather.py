from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"


async def make_nws_request(url: str) -> dict[str, Any] | None:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


def format_alert(feature: dict) -> str:
    props = feature["properties"]

    return f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description')}
Instructions: {props.get('instruction', 'No instructions')}
"""


@mcp.tool()
async def get_alerts(state: str) -> str:
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "Unable to fetch alerts."

    if len(data["features"]) == 0:
        return "No active alerts."

    alerts = [format_alert(f) for f in data["features"]]

    return "\n----------------\n".join(alerts)


@mcp.resource("echo://{message}")
def echo_resource(message: str) -> str:
    return f"Resource echo: {message}"

@mcp.prompt()
def greet_user(name: str) -> str:
    return f"""
You are a friendly weather assistant.

Greet the user named {name} politely.
Then ask which US state they want weather alerts for.
Suggest using the get_alerts tool to help them.
"""

# ⭐ ENTRY POINT
if __name__ == "__main__":
    mcp.run()