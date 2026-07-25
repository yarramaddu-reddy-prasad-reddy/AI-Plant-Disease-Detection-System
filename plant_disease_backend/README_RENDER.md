Render deployment instructions (backend)

1. Create a new **Web Service** on Render and connect your GitHub repo `AI-Plant-Disease-Detection-System`.

2. In the service settings:
   - **Root directory**: set to `plant_disease_backend` (this tells Render to use that subfolder).
   - **Environment**: `Python`.
   - **Branch**: `main` (or your chosen branch).

3. Build & Start commands:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT wsgi:app`

4. Runtime: we include `runtime.txt` in `plant_disease_backend` with `python-3.11.9` to ensure TensorFlow installs successfully.

5. Environment variables (set these in Render's dashboard -> Environment):
   - `DATABASE_URL` — your Postgres URL (if using DB), example: `postgresql://user:pass@host:port/dbname?sslmode=require`
   - `JWT_SECRET_KEY` — secret key for JWT tokens
   - Any other secrets your app requires (email creds, API keys, etc.)

6. Notes:
   - If you prefer using the repo root, set the service root accordingly and ensure `runtime.txt` is present at the chosen root (we added one at repo root too).
   - For logs and troubleshooting, check the Render build logs for package install errors (common with TF versions if Python version mismatches).
