# 🤖 Domain Expert LLM Chatbot for Machine Learning

## Project Description
Understanding Machine Learning concepts requires clear explanations, structured reasoning, and domain-specific guidance. Generic chatbots often provide broad or inconsistent responses that lack technical depth.

This project implements a **Domain Expert LLM Chatbot** designed to function strictly as a **Machine Learning expert assistant**. The system integrates a large language model (LLM) via API and uses **prompt engineering** to constrain responses to Machine Learning concepts, ensuring clarity, correctness, and relevance for academic and project-oriented use cases.

---

## Key Goals
- Enforce Machine Learning domain expertise in chatbot responses  
- Provide structured, step-by-step explanations of ML concepts  
- Build a modular and extensible AI system  
- Demonstrate real-world LLM integration using APIs  

---

## Objectives
- Assist students in learning Machine Learning theory and algorithms  
- Apply prompt engineering to control LLM behavior  
- Design a clean client–server architecture using FastAPI  
- Enable future enhancements such as memory and document-based querying  

---

## System Architecture
- **Frontend:** Web-based chat interface for user interaction  
- **Backend:** FastAPI service handling API requests and responses  
- **LLM Layer:** API-based large language model  
- **Control Mechanism:** Prompt engineering for domain restriction  

---

## Project Structure
```text
Domain-Expert-LLM-Chatbot/
│
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── prompt.py               # System and domain prompts
│   ├── requirements.txt        # Backend dependencies
│
├── frontend/
│   ├── index.html              # Chat interface
│   ├── style.css               # UI styling
│   └── script.js               # Frontend logic
│
├── README.md                   # Project documentation
└── .gitignore                  # Ignored files
