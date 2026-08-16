# Skill Map Agent 🤖

An AI-powered career assistant that uses **Gemini, Tavily Search, and JSearch/RapidAPI** to help users explore current industry skills and find relevant job and internship opportunities.

## 🚀 Features

- 🔎 **Web Search** — Uses Tavily to search the web for current information.
- 💼 **Job Search** — Uses JSearch through RapidAPI to find jobs and internships.
- 🤖 **AI Agent** — Gemini decides which tool to use based on the user's query.
- 📍 **Location-based Search** — Search for opportunities based on skills and location.
- 🎓 **Internship Search** — Supports finding full-time and internship opportunities.
- 🔐 **Environment Variables** — API keys are securely stored using `.env`.

## 🏗️ Architecture

```text
                    User Query
                        │
                        ▼
                Gemini AI Agent
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
       Tavily Search          Job Search Tool
             │                     │
             ▼                     ▼
        Web Search           JSearch API
                                   │
                                   ▼
                              RapidAPI
             │                     │
             └──────────┬──────────┘
                        ▼
                  Gemini Agent
                        │
                        ▼
                  Final Response
