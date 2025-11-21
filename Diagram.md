```mermaid
  flowchart LR
      %% Frontend
      subgraph Frontend
          UI[Web App<br/>Next.js/React]
      end
  
      %% Backend API
      subgraph Backend
          API[Backend API<br/>(FastAPI/Node)]
          ORCH[Agentic Orchestrator<br/>FINANCIERO PRO Agent]
  
          subgraph Ingestion
              UP[File Upload Service]
              S3[(S3<br/>raw_statements)]
              ING[Lambda/Worker<br/>Ingestion & Parsing]
          end
  
          subgraph DataLayer
              DB[(PostgreSQL<br/>Core Financial DB)]
              VS[(Vector Store<br/>(Futuro))]
          end
  
          subgraph Analytics
              CAT[Categorization Engine<br/>(Rules + LLM)]
              ANA[Spending Analytics<br/>(MVP)]
              PORT[Portfolio Engine<br/>(Futuro)]
              FI[FI Planner Engine<br/>(Futuro)]
          end
  
          subgraph Output
              PDF[Report Service<br/>(PDF Generator - Futuro)]
              NOTIF[Notification Service<br/>(Email/Push)]
          end
  
          SCHED[Scheduler<br/>(cron/EventBridge/n8n)]
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
