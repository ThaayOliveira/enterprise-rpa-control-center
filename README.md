# 📌 Visão Geral

O **Enterprise RPA Control Center** foi desenvolvido para centralizar esses processos em uma única plataforma, permitindo:

✅ execução manual de bots  
✅ execução automática via scheduler  
✅ monitoramento operacional  
✅ histórico de execuções  
✅ métricas em tempo real  
✅ rastreabilidade completa  

# Objetivo

Empresas possuem processos manuais repetitivos e sujeitos a erro.

# Solução

Plataforma centralizada para automações com monitoramento.

# Benefícios
redução de tempo operacional
rastreabilidade
escalabilidade
menor erro humano
execução agendada

# 🚀 Principais Funcionalidades

## Dashboard Executivo

Painel web com indicadores operacionais:

- total de execuções
- quantidade de sucessos
- falhas
- tempo médio
- histórico de execuções

---

## Bots Disponíveis

### 📄 Report Bot

Bot Selenium que:

- acessa sistema web
- realiza login automático
- valida acesso
- gera screenshot de evidência

### ❤️ Health Bot

Verifica disponibilidade de websites.

### 📡 Monitor Bot

Monitora tempo de resposta de serviços web.

### 📊 Reconcile Bot

Executa conciliação entre bases de dados simuladas e detecta divergências.

---

## Scheduler Automático

Execução recorrente automática via APScheduler.

Exemplo:

- bot executado a cada 5 minutos

---

# 🧱 Arquitetura

Dashboard (Streamlit)
        ↓
API REST (FastAPI)
        ↓
Bot Service (Orquestração)
        ↓
Bots Registry
        ↓
Bots RPA / Automação
        ↓
SQLite + Logs

# Comandos
uvicorn app.main:app --reload    ----> swagger
streamlit run dashboard/dashboard.py
docker compose up --build    ---> subir no docker