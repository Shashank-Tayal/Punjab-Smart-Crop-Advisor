import time
from google import genai

# Initialize the modern client with your API key
client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

def fetch_weather_data(district):
    print(f"[*] Fetching live meteorological data for {district}...")
    time.sleep(1) # Simulating network delay
    return {"temp": 34, "humidity": 65, "condition": "Partly Cloudy", "rainfall_chance": "20%"}

def fetch_soil_data(district):
    print(f"[*] Retrieving soil health metrics for {district}...")
    time.sleep(1)
    return {"type": "Alluvial", "ph": 7.2, "nitrogen": "Low", "phosphorus": "Medium", "potassium": "High"}

def generate_advisory(crop, weather, soil):
    print("[*] Running AI analysis for small/marginal farmer advisory...\n")
    
    prompt = f"""
    Act as an agricultural expert for the Government of Punjab. 
    A small/marginal farmer is growing {crop}. 
    Current weather: {weather['temp']}°C, {weather['condition']}, Humidity {weather['humidity']}%.
    Soil status: {soil['type']} soil, pH {soil['ph']}, Nitrogen is {soil['nitrogen']}.
    Provide a concise, 3-bullet-point advisory actionable for a farmer with limited resources.
    """
    
    # Using the new SDK syntax
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    return response.text

def main():
    print("="*60)
    print("   SMART CROP ADVISORY SYSTEM - PUNJAB GOVT (PROTOTYPE)   ")
    print("                   Release: Shankz.exe                    ")
    print("="*60)
    
    district = input("Enter Farming District (e.g., Ludhiana, Patiala): ")
    crop = input("Enter Current Crop (e.g., Paddy, Wheat, Cotton): ")
    
    print("-" * 60)
    weather = fetch_weather_data(district)
    soil = fetch_soil_data(district)
    
    advisory = generate_advisory(crop, weather, soil)
    
    print("="*60)
    print(" FINAL ADVISORY OUTPUT ")
    print("="*60)
    print(f"Location: {district.upper()} | Crop: {crop.upper()}")
    print(f"Weather: {weather['temp']}°C, {weather['condition']}")
    print(f"Soil Health: pH {soil['ph']}, NPK Status: {soil['nitrogen']}/{soil['phosphorus']}/{soil['potassium']}")
    print("-" * 60)
    print(advisory)
    print("="*60)

if __name__ == "__main__":
    main()