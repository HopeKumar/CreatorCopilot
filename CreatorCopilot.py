"""
CreatorCopilot
Multi-agent AI system for YouTube content planning and script generation.

Built as a capstone project for the Kaggle x Google AI Agents Intensive.
"""

# ============================================================
# CreatorCopilot: Robust Version
# Handles:
# - Missing API keys
# - 404 model errors
# - 429 quota / rate-limit errors
# ============================================================

import os
import time
import random
import pandas as pd
import google.generativeai as genai

# Kaggle secrets are optional (only available on Kaggle)
try:
    from kaggle_secrets import UserSecretsClient
    KAGGLE_AVAILABLE = True
except ImportError:
    KAGGLE_AVAILABLE = False

# ------------------ API KEY SETUP (SAFE) --------------------

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY and KAGGLE_AVAILABLE:
    try:
        user_secrets = UserSecretsClient()
        GEMINI_API_KEY = user_secrets.get_secret("GEMINI_API_KEY")
        print("API key loaded from Kaggle Secrets.")
    except Exception:
        GEMINI_API_KEY = None

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    print("WARNING: No API key found. Running in mock mode.")

# ------------------ MODEL SELECTION ------------------------

MODEL_ID = "models/gemini-1.5-flash"

if GEMINI_API_KEY:
    try:
        available_models = [m.name for m in genai.list_models()]
        if "models/gemini-2.5-flash" in available_models:
            MODEL_ID = "models/gemini-2.5-flash"
        print(f"Using model: {MODEL_ID}")
    except Exception:
        print("Model listing failed. Falling back to default model.")

# ------------------- LLM CALL HELPER -----------------------

def call_llm(system_prompt: str, user_prompt: str, max_retries: int = 5) -> str:
    """
    Calls Gemini with retry + exponential backoff for rate limits (429).
    Returns mock output if API key is missing.
    """

    if not GEMINI_API_KEY:
        return "Mock Response: API key not configured."

    model = genai.GenerativeModel(
        model_name=MODEL_ID,
        system_instruction=system_prompt
    )

    for attempt in range(max_retries):
        try:
            response = model.generate_content(user_prompt)
            return (response.text or "").strip()

        except Exce
