# ChurchPad Subscription and Notification System

A simple backend service to manage livestream subscriptions for churches. Subscribers can register, get billed via Stripe, and receive a welcome SMS asynchronously via Twilio and Celery.

---

## Features

- ✅ Subscribe to livestream plans (`POST /subscribe/`)
- ✅ List all active subscriptions (`GET /subscription/`)
- ✅ Cancel a subscription (`DELETE /unsubscribe/<id>/`)
- ✅ Send welcome SMS using Twilio (async via Celery + Redis)
- ✅ User authentication (`/api/users/token/`)
- ✅ Auto-generated OpenAPI docs via DRF Spectacular
- ✅ Postman collection for easy API testing

---

## 🚀 Tech Stack

- Django + Django REST Framework
- PostgreSQL (or SQLite for dev)
- Stripe (Test Mode)
- Twilio (Sandbox or real credentials)
- Celery with Redis as message broker
- DRF Spectacular for API docs

---

## ⚙️ Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/churchpad-subscription.git
cd churchpad-subscription
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root with the following content:

```env
SECRET_KEY=your-secret-key
DEBUG=True
STRIPE_SECRET_KEY=your-stripe-test-key
TWILIO_ACCOUNT_SID=your-twilio-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_PHONE_NUMBER=your-twilio-phone
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Start Redis Server (required for Celery)

Ensure Redis is running. You can use Docker for a quick setup:
install Redis natively based on your OS.

### 7. Start Celery Worker (in a new terminal)

```bash
celery -A core worker --loglevel=info
```

Make sure Redis is running before starting the Celery worker.

### 8. Run the Development Server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/
