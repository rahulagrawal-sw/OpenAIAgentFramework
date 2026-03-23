# OpenAIAgentFramework
AI Agents and AgenticAI using OpenAI Agent Framework

This is experimentation zone to try
-- Agentic AI
-- AI Agent
-- Multi Modal AI Agents
-- LLM
-- etc

Steps followed during project development
<ul>
python -m venv .venv
#.\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
.\.venv\Scripts\pip.exe install -r .\requirements.txt
c:\ML\OpenAIAgentFramework\.venv\Scripts\python.exe -c "from fastapi import FastAPI; print('OK')"
Creating .vscode/settings.json to set the project's Python interpreter to the project .venv:
c:\ML\OpenAIAgentFramework\.venv\Scripts\python.exe -m uvicorn src.main:app --host 127.0.0.1 --port 8000
Start-Sleep -Seconds 2; Invoke-WebRequest -Uri http://127.0.0.1:8000/ -UseBasicParsing | Select-Object -ExpandProperty Content
</ul>

-----------------------------------------------------------------------------------------------------------------------------------

Go inside folder "/c/ML/OpenAIAgentFramework"
.venv/Scripts/Activate
pip.exe install -r requirements.txt

python.exe -m uvicorn src.main:app --host 127.0.0.1 --port 8000

open browser and paste url "http://127.0.0.1:8000/run/finance_agent?input_query=Suggest%20top%202%20companies%20to%20invest%20in%20NSE%20India"
Search term: Suggest top 2 companies to invest in NSE India

-----------------------------------------------------------------------------------------------------------------------------------
python src/memory/sqllite_session.py