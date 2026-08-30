# Punjab Smart Crop Advisor 🌾

**Release:** Shankz.exe 
**Event:** Smart India Hackathon (SIH) 2026 - Internal College Round (Arya College)

## The Problem
Small and marginal farmers in Punjab often lack access to hyper-localized, easy-to-understand agricultural data. I built this prototype for a Smart India Hackathon problem statement to bridge that gap. The goal was to provide enterprise-level farming intelligence in a lightweight, accessible format requiring minimal user input.

## The Solution (Prototype)
A Python-based console application that takes basic inputs (District and Crop) and generates a highly specific, low-cost action plan for the farmer. 

**Core Features:**
* **API Integration:** Simulates fetching live meteorological data and soil health metrics (pH, NPK).
* **AI Engine:** Feeds environmental data into the `google-genai` (Gemini) API to generate a context-aware, 3-point agricultural advisory.
* **Resilient Architecture:** Features an automated error-handling loop that instantly reroutes to a backup AI model if the primary server experiences high traffic (Error 503).
* **Offline Accessibility:** Automatically generates and opens a `.txt` report of the advisory, ensuring local village centers can easily share the data via SMS or WhatsApp in areas with poor internet connectivity.

## Tech Stack
* **Language:** Python 3.12
* **AI:** Google Gemini API (Models: 3.7-flash, 2.5-flash)

## The Hackathon Journey & Lessons Learned
This project was pitched during the SIH 2026 internal hackathon. While the underlying logic and architecture were solid, the live presentation was a massive learning experience:

1. **The Live Demo Curse:** During the pitch, I experienced a severe network glitch. I had to troubleshoot the connection live under pressure. It eventually worked, teaching me the critical importance of building offline fallbacks and caching for live demos.
2. **The "AI" Buzzword Trap:** The judges became hyper-focused on the word "AI," leading to irrelevant questions that derailed the actual technical pitch. I learned that when presenting technical software to a mixed panel, it is often better to focus on the *impact* and the *logic flow* rather than the specific buzzwords driving the backend.
3. **Subjectivity vs. Code:** We didn't make the top 50, and our presentation delivery wasn't perfect. But the code works, the error handling is robust, and the core problem is solved. Hackathon results are subjective, but a working codebase is objective. 

This repository serves as a post-mortem of that experience—showcasing not just the code, but the resilience required to build and present it.

## How to Run Locally
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Insert your Google Gemini API key into `main.py`.
4. Run `python main.py` and follow the console prompts.
