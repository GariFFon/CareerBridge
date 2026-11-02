# 🌉 CareerBridge

> **Academia–Industry Collaboration Portal**  
> SIH26044 · Ministry of Ayush

CareerBridge is a full-stack web platform that bridges the gap between students, universities, and companies — enabling seamless internship discovery, skill-based matching, and application management.

---

## ✨ Features

- 🔐 **Role-based Authentication** — Students, Companies, Universities, and Admins with JWT tokens
- 🎯 **Smart Skill Matching** — Rule-based algorithm scores internships against student skills (required skills weighted 3×)
- 📋 **Internship Management** — Companies can post, manage, and close internship listings (On-site / Hybrid / Remote)
- 📨 **Application Tracking** — Students apply, track status; companies review and respond
- 🏛️ **Institution Dashboard** — Universities oversee their students' profiles and placements
- 📊 **Analytics Module** — Platform-wide insights and engagement data
- 🌗 **Dark / Light Mode** — Full theme support across the frontend

---

## 🏗️ Tech Stack

### Backend
| Layer | Technology |
|-------|-----------|
| Framework | Django 6.1 + Django REST Framework 3.18 |
| Auth | JWT via `djangorestframework-simplejwt` |
| Database | PostgreSQL (production) / SQLite (dev) |
| Storage | Pillow + WhiteNoise for media & static files |
| CORS | `django-cors-headers` |
| Config | `python-decouple` (`.env` based) |
| Server | Gunicorn |

### Frontend
| Layer | Technology |
|-------|-----------|
| Framework | Next.js 16 + React 19 |
| Language | TypeScript 5 |
| Styling | Tailwind CSS 4 |
| UI Components | shadcn/ui + Radix UI |
| Charts | Recharts |
| Tables | TanStack Table v9 |
| Drag & Drop | dnd-kit |
| Notifications | Sonner |
| Schema Validation | Zod |

---

## 📁 Project Structure

```
CareerBridge/
├── accounts/               # Custom user model & role-based auth
├── institutions/           # University & Company profiles
├── internships/            # Listings, skills & matching algorithm
├── applications/           # Student applications & status tracking
├── analytics/              # Platform analytics & reporting
├── careerbridge-backend/   # Django project config (settings, urls, wsgi)
├── careerbridge-frontend/  # Next.js frontend app
│   └── src/
│       ├── app/            # Next.js App Router pages
│       ├── components/     # Reusable UI components
│       ├── contexts/       # Auth context
│       └── lib/            # API client, utilities, hooks
├── manage.py
├── requirements.txt
└── CareerBridge_SRS_Report.docx
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Node.js 20+
- PostgreSQL (for production) or SQLite (dev, zero config)

---

### 🐍 Backend Setup

```bash
# 1. Clone the repo
git clone https://github.com/GariFFon/CareerBridge.git
cd CareerBridge

# 2. Create & activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cp .env.example .env            # Then fill in your values
```

**`.env` variables:**
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Leave empty to use SQLite in dev
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# CORS — allow the Next.js dev server
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

```bash
# 5. Apply migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser
# or use the helper script:
python create_superuser.py

# 7. Start the dev server
python manage.py runserver
```

Backend runs at → **http://localhost:8000**  
Admin panel → **http://localhost:8000/admin**

---

### ⚛️ Frontend Setup

```bash
cd careerbridge-frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

Frontend runs at → **http://localhost:3000**

---

## 🔌 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `POST /api/token/` | Obtain JWT access + refresh tokens |
| `POST /api/token/refresh/` | Refresh access token |
| `api/accounts/` | User registration, profiles |
| `api/institutions/` | University & company management |
| `api/internships/` | Internship CRUD + skill matching |
| `api/applications/` | Apply, track & manage applications |
| `api/analytics/` | Platform stats & reports |

---

## 🧠 Skill Matching Algorithm

The matching engine compares a student's skill set against an internship's requirements:

- **Required skills** are weighted **3×**
- **Preferred skills** are weighted **1×**
- Score = `(matched_required × 3 + matched_preferred × 1) / max_possible × 100`

The top-N ranked internships are surfaced as recommendations on the student dashboard.

---

## 👥 User Roles

| Role | Capabilities |
|------|-------------|
| **Student** | Browse & apply to internships, get skill-matched recommendations |
| **Company** | Post internships, review applications, manage listings |
| **University** | View student profiles, track placements, manage institution |
| **Admin** | Full platform access via Django admin |

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is developed as part of **Smart India Hackathon (SIH26044)** for the **Ministry of Ayush**.

---

<div align="center">
  Made with ❤️ by Team CareerBridge
</div>
