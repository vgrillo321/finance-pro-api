# 💸 FINANCIERO PRO — Grillo FI Agent

> Personal financial OS for **Victor Grillo** — bookkeeper, spending analytics & (futuro) investment + FI planner powered by Agentic AI.

FINANCIERO PRO es un sistema diseñado para centralizar tus finanzas personales y de inversión:

- 📥 Ingesta automática de **statements** (Chase, Capital One, Discover, brokers)
- 🧮 Normalización y clasificación inteligente de gastos
- 📊 Dashboards con resumen mensual
- 🎯 Base para un **Investment Agent** y **FI Planner** (FIRE, proyecciones, rebalance)

Este README documenta:

- Arquitectura high-level (gráfica con Mermaid)
- Alcance del **MVP (Fase 1 — Bookkeeper)**
- Plan de implementación (checklist por semanas)
- Roadmap de futuras fases (Investment AI & FI Planner)

---

## 🧭 Table of Contents

1. [Vision & Goals](#-vision--goals)
2. [High-Level Architecture](#-high-level-architecture)
3. [Repositories & Tech Stack](#-repositories--tech-stack)
4. [Phase 1 Scope — Bookkeeper MVP](#-phase-1-scope--bookkeeper-mvp)
5. [Implementation Plan (1-Month MVP)](#-implementation-plan-1-month-mvp)
6. [Getting Started (Dev Setup)](#-getting-started-dev-setup)
7. [Roadmap (Future Phases)](#-roadmap-future-phases)

---

## 🎯 Vision & Goals

**FINANCIERO PRO** aims to be:

> _“YNAB + Personal Capital + Vanguard Advisor… pero 100% personalizado para Victor Grillo y sin pagarle a nadie.”_

Core objectives:

- Consolidar gastos de cuentas y tarjetas en un solo lugar.
- Clasificar gastos de forma automática (fast food, groceries, gasolina, weed, health, home improvement, etc.).
- Permitir reclasificación manual rápida (para entrenar el sistema).
- Producir un resumen mensual claro de:
  - Total gasto
  - Gasto por categoría
  - Tendencias vs meses anteriores
  - Ahorro estimado

Fase 1 se centra en el rol de **Bookkeeper inteligente**.  
Fases futuras añadirán:

- 🔮 Investment Agent (Rebalance, compra recomendada, riesgo, proyección de portafolio).
- 🔥 FI Planner (FIRE number, savings rate, “retire at 39 vs 38 si bajas fast food 20%”).

---

## 🏗️ High-Level Architecture

La arquitectura está pensada en capas: Frontend, Backend/API, Ingesta, Data Layer, Analytics y Output/Notificaciones.  
El objetivo es que esta base soporte luego los agentes de inversión y FI sin reescribir todo.

```mermaid
flowchart LR
    %% Frontend
    subgraph Frontend
        UI["Web App (Next.js/React)"]
    end

    %% Backend API
    subgraph Backend
        API["Backend API (FastAPI/Node)"]
        ORCH["Agentic Orchestrator - FINANCIERO PRO Agent"]

        subgraph Ingestion
            UP["File Upload Service"]
            S3[("S3 raw_statements")]
            ING["Lambda/Worker - Ingestion & Parsing"]
        end

        subgraph DataLayer
            DB[("PostgreSQL - Core Financial DB")]
            VS["Vector Store (Futuro)"]
        end

        subgraph Analytics
            CAT["Categorization Engine (Rules + LLM)"]
            ANA["Spending Analytics (MVP)"]
            PORT["Portfolio Engine (Futuro)"]
            FI["FI Planner Engine (Futuro)"]
        end

        subgraph Output
            PDF["Report Service (PDF Generator - Futuro)"]
            NOTIF["Notification Service (Email/Push)"]
        end

        SCHED["Scheduler (cron / EventBridge / n8n)"]
    end

    %% Flujos principales
    UI -->|Upload PDFs/CSVs| API --> UP --> S3 --> ING
    ING -->|Transacciones limpias| DB

    API --> ORCH
    ORCH --> CAT
    CAT --> DB
    ORCH --> ANA
    ANA --> DB

    %% Futuro: portfolio, FI, reportes
    ORCH --> PORT
    ORCH --> FI
    ORCH --> PDF
    ORCH --> NOTIF

    SCHED --> ORCH
    UI -->|Dashboards & Queries| API --> DB
