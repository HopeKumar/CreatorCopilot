# CreatorCopilot
**Multi-Agent AI System for YouTube Content Planning & Script Drafting**

CreatorCopilot is an agent-based Generative AI system that automates the YouTube pre-production workflow for solo creators.  
It transforms creator intent into **production-ready video ideas, structured briefs, short-form scripts, and thumbnail concepts** in minutes.

This project was built as a **capstone for the Kaggle x Google AI Agents Intensive Program**.

---

## 🚀 Features
- Automated content ideation based on niche, audience, and goals  
- Structured video planning with hooks and outlines  
- Short-form script generation optimized for YouTube Shorts  
- Thumbnail text and visual concept suggestions  
- Multi-agent orchestration for consistent outputs  
- Robust handling of API rate limits and model availability  

---

## 🧠 Agent Architecture

CreatorCopilot simulates a small content team using specialized AI agents:

1. **Ideation Agent**  
   Generates multiple video ideas with attention-grabbing hooks.

2. **Planning Agent**  
   Converts selected ideas into actionable video briefs.

3. **Scriptwriter Agent**  
   Writes concise, high-energy scripts suitable for short-form content.

4. **Thumbnail Copy Agent**  
   Suggests short thumbnail text and visual direction.

Each agent operates independently while sharing structured context through the pipeline.

---

## 🔁 Workflow

```
User Input
↓
Ideation Agent
↓
Planning Agent
↓
Scriptwriter Agent
↓
Thumbnail Copy Agent
↓
Production-Ready Content
```

---

## 🛠️ Tech Stack
- **Language:** Python  
- **LLM:** Gemini API  
- **Environment:** Kaggle Notebook / Local Python  
- **Architecture:** Prompt-chained multi-agent pipeline  
- **State Management:** Session-level context passing  
- **Data Handling:** Pandas  

---

## 📂 Repository Structure
```
creatorcopilot-ai-agent/
├── creatorcopilot.py # Main execution script
├── creatorcopilot.ipynb # Notebook version (Kaggle)
├── requirements.txt # Dependencies
└── README.md
```
---

## ⚙️ Setup & Installation

```bash
pip install -r requirements.txt
```
## 🔑 API Key Setup

CreatorCopilot uses the Gemini API.

### Kaggle

Add a Kaggle Secret named: ``` GEMINI_API_KEY ```
The project automatically reads it.

### Local Usage

Linux / macOS
```
export GEMINI_API_KEY="your_api_key_here"
```

Windows (PowerShell)
```
setx GEMINI_API_KEY "your_api_key_here"
```
If no API key is found, the system runs in mock mode.

▶️ How to Run
```
python creatorcopilot.py
```
The script generates content for multiple niches and saves the output to a CSV file.

📌 Example Use Case
Input
```
 Niche: Minecraft Survival
Audience: Beginner Players
Goal: Day 1 Survival
```

Output

Video ideas with hooks

Structured briefs

45-second scripts

Thumbnail text and visual concepts

👤 Author

J Hope Kumar
📧 kumarhope2018@gmail.com

🔗 LinkedIn: https://linkedin.com/in/12HOPE

