import requests
from datetime import datetime

def get_weather():
    try:
        response = requests.get("https://wttr.in/?format=j1")
        data = response.json()
        temp = data["current_condition"][0]["temp_C"]
        return f"Temperature: {temp}°C"
    except:
        return "Weather unavailable"

def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()
        quote = data[0]["q"]
        author = data[0]["a"]
        return f'"{quote}" - {author}'
    except:
        return "Quote unavailable"

def build_summary():
    weather = get_weather()
    quote = get_quote()
    today = datetime.now().strftime("%d-%m-%Y")

    report = f"""
==========================
      PULSE REPORT
==========================

Date: {today}

WEATHER
{weather}

QUOTE
{quote}
"""

    with open("summary.txt", "w", encoding="utf-8") as file:
        file.write(report)

    print("Summary created successfully!")

build_summary()
