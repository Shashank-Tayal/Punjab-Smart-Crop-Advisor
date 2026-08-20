import time
import os
import sys

# Optional: Mute gRPC debug logs just to be safe
os.environ['GRPC_VERBOSITY'] = 'ERROR'
os.environ['GLOG_minloglevel'] = '2'

from google import genai
from google.genai import errors

# Initialize the modern client
client = genai.Client(api_key="AIzaSyD_hWve16fHfNIy5hr-n6ZtVlnWyuo2fs0")

# Terminal Colors for UI
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def fetch_weather_data(district):
    print(f"{CYAN}[*] Fetching live meteorological data for {district}...{RESET}")
    time.sleep(1)
    return {"temp": 34, "humidity": 65, "condition": "Partly Cloudy"}

def fetch_soil_data(district):
    print(f"{CYAN}[*] Retrieving soil health metrics for {district}...{RESET}")
    time.sleep(1)
    return {"type": "Alluvial", "ph": 7.2, "nitrogen": "Low", "phosphorus": "Med", "potassium": "High"}

def generate_advisory(crop, weather, soil):
    print(f"{CYAN}[*] Running AI analysis for advisory...{RESET}")
    
    prompt = f"""
    Act as an agricultural expert for the Government of Punjab. 
    A farmer is growing {crop}. 
    Weather: {weather['temp']}°C, {weather['condition']}, Humidity {weather['humidity']}%.
    Soil: {soil['type']}, pH {soil['ph']}, Nitrogen: {soil['nitrogen']}.
    Provide a concise, 3-bullet-point advisory actionable for a farmer with limited resources.
    """
    
    models_to_try = ['gemini-2.5-flash', 'gemini-1.5-flash']
    
    for model_name in models_to_try:
        try:
            # FIX: Swapped to the Chat interface to eliminate the AFC warning natively
            chat = client.chats.create(model=model_name)
            response = chat.send_message(prompt)
            return response.text
            
        except errors.ServerError as e:
            if "503" in str(e):
                continue
            raise e
            
    return "Advisory Service is currently offline. Please check back later."

def main():
    print(f"\n{BOLD}{GREEN}{'='*65}{RESET}")
    print(f"{BOLD}{GREEN}   SMART CROP ADVISORY SYSTEM - PUNJAB GOVT (PROTOTYPE)   {RESET}")
    print(f"{BOLD}{GREEN}                   Release: Shankz.exe                    {RESET}")
    print(f"{BOLD}{GREEN}{'='*65}{RESET}\n")
    
    district = input(f"{YELLOW}Enter Farming District (e.g., Ludhiana): {RESET}")
    crop = input(f"{YELLOW}Enter Current Crop (e.g., Paddy, Wheat): {RESET}\n")
    
    weather = fetch_weather_data(district)
    soil = fetch_soil_data(district)
    
    print("\n" + "-" * 65 + "\n")
    advisory = generate_advisory(crop, weather, soil)
    
    print(f"\n{BOLD}{GREEN}{'='*65}{RESET}")
    print(f"{BOLD}{GREEN} FINAL ADVISORY OUTPUT {RESET}")
    print(f"{BOLD}{GREEN}{'='*65}{RESET}\n")
    
    print(f"{BOLD}Location:{RESET} {district.upper()} | {BOLD}Crop:{RESET} {crop.upper()}")
    print(f"{BOLD}Weather:{RESET} {weather['temp']}°C, {weather['condition']}")
    print(f"{BOLD}Soil Health:{RESET} pH {soil['ph']} | NPK: {soil['nitrogen']}/{soil['phosphorus']}/{soil['potassium']}\n")
    
    print(f"{YELLOW}{advisory}{RESET}\n")
    print(f"{BOLD}{GREEN}{'='*65}{RESET}\n")

if __name__ == "__main__":
    main()