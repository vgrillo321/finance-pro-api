# 💸 FINANCIERO PRO — Grillo FI Agent

> Personal financial OS for **Victor Grillo** — bookkeeper, spending analytics & (futuro) investment + FI planner powered by Agentic AI.

FINANCIERO PRO es un sistema creado para convertir tus finanzas personales en un ecosistema inteligente que:

- Lee y procesa tus statements  
- Clasifica tus gastos automáticamente  
- Te da insights sobre tus hábitos financieros  
- Sienta la base para un verdadero **Investment AI** y un **FI Planner**  

Este README documenta **todo lo necesario para construir la Fase 1 (MVP – Bookkeeper)**.

---

# 🧠 En Fase 1 (MVP) realmente vas a usar:

- **UI** (Web App – Next.js)
- **API** (Backend – FastAPI/Nest)
- **UP, S3, ING** (Ingesta básica)
- **DB** (PostgreSQL)
- **CAT** (Categorization Engine v1 – reglas)
- **ANA** (Spending Analytics simple)

🧩 El resto queda como **futuro**, pero el sistema ya está pensado para crecer sin romper nada.

---

# 📂 Repositories & Tech Stack

## Repositorios

### **`financiero-api`**
Backend principal que maneja:

- Ingesta de archivos  
- Parsers  
- Endpoints de transacciones y resúmenes  
- Lógica de categorización y analytics  

### **`financiero-web`**
Frontend (Next.js/React) con:

- Dashboard  
- Upload de statements  
- Vista de transacciones  
- Resúmenes mensuales  

💡 **Estos repos NO son solo para el Bookkeeper:**  
Son la **base de todo el sistema**, incluyendo:

- Investment Agent  
- FI Planner  
- Report Engine  
- Alertas Agentic  

---

## 🛠️ Tech Stack sugerido

### Backend (`financiero-api`)
- Python (FastAPI) **o** Node.js (NestJS)
- PostgreSQL
- Migraciones:
  - Alembic (Python)  
  - Prisma (Node)
- Parsing:
  - `pandas`, `csv`
  - `pdfplumber` / `camelot` (para PDFs)

### Frontend (`financiero-web`)
- Next.js (React)
- Tailwind CSS
- Recharts / Chart.js para gráficas

### Infra (futuras fases)
- AWS S3  
- AWS Lambda / ECS  
- AWS RDS/Aurora  
- EventBridge  
- n8n (opcional)  

---

# 📌 Phase 1 Scope — Bookkeeper MVP

## 🎯 Meta en 1 mes:

Un sistema funcional donde puedas:

- Subir statements (CSV funcional)
- Parsearlos y guardarlos en PostgreSQL
- Autoclasificar gastos con reglas simples
- Reclasificar manualmente desde la UI
- Ver desglose mensual por categoría
- Ver insights básicos como:

> “Fast food fue 25% de tu gasto variable en noviembre.”

---

## Componentes incluidos:

- Ingesta de archivos (CSV; PDF opcional)
- Parsers por banco
- Normalización de transacciones
- Base de datos financiera
- Categorization Engine v1 (rules-based)
- Spending Analytics (sumas + charts)
- UI básica (dashboard + tabla)

---

# ✅ Implementation Plan (1-Month MVP)

## 🟦 Semana 1 — Fundaciones

### Infraestructura & Setup
- [✅] Crear repos: `financiero-api`, `financiero-web`
- [✅ ] Configurar entorno backend (FastAPI / NestJS)
- [ ] Configurar entorno frontend (Next.js)
- [ ] Configurar PostgreSQL (local o docker)
- [ ] Añadir migraciones iniciales

### Esquema DB inicial
Tablas:

- [ ] `users`
- [ ] `accounts`
- [ ] `categories` (seed inicial)
- [ ] `transactions`  
  Campos:
  - `id, user_id, account_id, date, amount, vendor, description, raw_source, category_id, is_business, created_at, updated_at`

### Back & Front mínimos
- [ ] Endpoint `GET /health`
- [ ] Endpoint mock `GET /transactions`
- [ ] Web:
  - [ ] Pantalla “login fake”
  - [ ] Dashboard vacío

---

## 🟩 Semana 2 — Ingesta y Parsing

### Upload & Storage
- [ ] Endpoint `POST /statements/upload`
- [ ] Aceptar CSV (PDF opcional)
- [ ] Guardar archivo localmente (S3 futuro)
- [ ] Detectar tipo/format (Chase vs Capital One)

### Parsers
- [ ] Parser CSV Chase
- [ ] Parser CSV Capital One (si hay tiempo)
- [ ] Normalización:

```json
{
  "date": "2025-11-12",
  "amount": -14.76,
  "vendor": "CHICK-FIL-A #123",
  "description": "POS Transaction",
  "raw_source": "Chase"
}
```
- [ ] Inserción masiva en `transactions`

### Frontend
- [ ] Form de upload
- [ ] Llamar `/statements/upload`
- [ ] Mostrar mensaje: “X transacciones procesadas”

---

## 🟨 Semana 3 — Clasificación & Vista de Gastos

### Transacciones
- [ ] Endpoint real `GET /transactions?...`
- [ ] Tabla:

  - Fecha  
  - Vendor  
  - Descripción  
  - Monto  
  - Categoría (editable)

### Categorization Engine v1
Reglas para:

- Fast food  
- Premium restaurants  
- Groceries (Giant, Safeway, Costco…)  
- Gasolina  
- Weed / alcohol  
- Gym / health  
- Home improvement  
- Real estate  

- [ ] Hook post-insert  
- [ ] PATCH `/transactions/{id}/category`
- [ ] Dropdown en UI

### Summary básico
- [ ] Endpoint `GET /summary/spending?month=YYYY-MM`
- [ ] Gráfico (pie/barras)

---

## 🟧 Semana 4 — MVP Completo & Polish

### Resumen mensual avanzado
- [ ] Endpoint `GET /summary/monthly`
  - Total gasto  
  - % por categoría  
  - Comparación vs mes anterior  
  - Ahorro estimado  

### Mini Insights
Backend genera:

- [ ] “Fast food = X% del gasto variable”  
- [ ] “Premium restaurants subió X% vs mes pasado”  
- [ ] “Gasto total subió/bajó X%”  

### UX & Quality
- [ ] Filtros rápidos (este mes / mes pasado / últimos 30 días)
- [ ] Loading states
- [ ] Manejo de errores (archivos inválidos)
- [ ] Mensajes claros

### Opcional
- [ ] Export PDF del resumen mensual

---

# 🚀 Getting Started (Dev Setup)

## Requisitos

- Node.js  
- Python 3.x (si usas FastAPI)  
- PostgreSQL  
- Git  
- Docker (opcional)  

---

## Pasos iniciales

```bash
git clone git@github.com:tu-org/financiero-api.git
git clone git@github.com:tu-org/financiero-web.git
```

Configurar `.env` en ambos proyectos.

---

### Crear DB con Docker

```bash
docker run --name financiero-db \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=financiero \
  -p 5432:5432 \
  -d postgres
```

### Correr backend & frontend

```bash
# Backend
cd financiero-api
uvicorn app.main:app --reload   # FastAPI ejemplo

# Frontend
cd ../financiero-web
npm install
npm run dev
```

# 📈 Roadmap (Future Phases)

## Phase 2 — Investment AI (Portfolio Agent)

- Holdings de Vanguard / Robinhood  
- Asset allocation actual y target  
- Riesgo básico  
- Rebalance con aporte mensual ($680)  
- Recomendaciones del tipo:

> “Compra 1.3 VTI, 0.9 VIG, 0.5 VYM.”

---

## Phase 3 — FI Planner & Agentic Mode

- FI number, Savings Rate, timeline FI  
- Escenarios:
  - Reducir fast food / premium / weed  
  - Cambios de ingreso  
- Agente Agentic:
  - Weekly Debrief  
  - Alertas  
  - Reporte mensual:
    **“Victor Grillo Financial Report — Noviembre 2025”**  

---

> _“Si sigues así, te retiras a los 39.  
> Si bajas fast food 20%, te retiras a los 38…”_  
>  
> — **FINANCIERO PRO**, futuro Dios Financiero 😎
