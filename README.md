# Sparly – Telegram Bot for Personal Discounts

Sparly is a Telegram bot that monitors promotional offers from major grocery and drugstore chains in Germany and delivers a personalised digest of the best deals to you twice a day. It also helps you compare prices for your shopping basket across nearby stores.

## Features

- **Daily digests**: Twice per day (09:00 and 18:00 Europe/Berlin), Sparly sends you a curated list of up to 40 promotions from supermarkets and discounters near your location.
- **Dynamic radius**: Choose a base radius (default 6 km); for large chains such as Kaufland and Globus the radius expands to 15 km automatically. Locations are stored in PostGIS and queried using `ST_DWithin` for efficient geospatial search.
- **Price comparison**: With the `/basket` command, supply a list of items and Sparly will show you which nearby store offers the cheapest basket.
- **Item tracking**: In future versions, users will be able to mark specific products to follow; Sparly will include all variants with good prices in the digest.
- **Multi‑language**: User interface is available in Ukrainian 🇺🇦, Russian 🇷🇺 and German 🇩🇪, configurable via `/start` or `/prefs`.
- **Trial & subscriptions**: Each Telegram account/device gets exactly one free 7‑day trial. Payment integration (e.g. LiqPay/Stripe) will be added later.

## Tech stack

- Python 3.11, [aiogram](https://docs.aiogram.dev/) 3
- PostgreSQL 15 with PostGIS for geospatial queries
- Redis for caching and trial flags
- Async scraping modules for each store (REWE, Lidl, Aldi, etc.)
- Tesseract OCR via `pytesseract` for PDF brochures
- Docker & Docker Compose
- GitHub Actions for CI

## Repository structure

```
sparly/
├── bot/                  # Bot entrypoint and handlers
│   ├── main.py
│   ├── handlers.py
│   └── utils/
│       ├── geo.py
│       └── trial.py
├── scrapers/             # One module per store
├── db/
│   ├── init.sql          # Initialise PostGIS and load schemas
│   └── models.sql        # Table definitions (stores, discounts, users)
├── translations.yaml     # Language strings (uk, ru, de)
├── docker-compose.yml    # Services for the bot, database and redis
├── Dockerfile            # Application image
├── requirements.txt
└── .github/workflows/
    └── ci.yml            # CI pipeline
```

## Running locally

1. **Clone the repository** and switch to the `init-skeleton` branch (or your working branch):

   ```bash
   git clone https://github.com/k0reets86/sparly.git
   cd sparly
   ```

2. **Configure environment variables**: create a `.env` file (not committed) with your `TELEGRAM_TOKEN` and any store API keys. For local development you can also provide `DATABASE_URL` and `REDIS_URL`, but `docker-compose.yml` already defines defaults.

3. **Start services** using Docker Compose:

   ```bash
   docker compose up --build
   ```

   This will build the bot image, start a PostGIS database (`db`), a Redis instance (`redis`) and run the bot (`web`). The bot will reconnect on file changes thanks to volume mounting.

4. **Initialise the database**:

   Once the database is up, run the migration script to create tables and enable PostGIS:

   ```bash
   docker compose exec db psql -U postgres -d sparly -f /app/db/init.sql
   ```

5. **Run the bot**: The bot starts automatically in the `web` service. You should see logs indicating that the bot has connected to Telegram. Use `/start` in your Telegram client to begin.

## Deploying to Render

Render can host the bot as a web service with a cron job for daily digests and provide a free PostgreSQL instance with PostGIS. Follow these steps:

1. **Create a new Web Service** on Render from your GitHub repository.
2. **Set environment variables** in Render’s dashboard: `TELEGRAM_TOKEN`, `DATABASE_URL`, `REDIS_URL` and any store credentials.
3. **Add a PostgreSQL database** (with PostGIS) and a Redis instance.
4. **Configure cron jobs** for sending digests at `0 9 * * *` and `0 18 * * *` (Berlin time).
5. **Deploy** and monitor logs via Render’s dashboard.

For more deployment details, see [Render’s documentation](https://docs.render.com/).

## License

This project is currently in development and not yet released under a specific license. All rights reserved by the author until further notice.
