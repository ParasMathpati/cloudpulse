from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="CloudPulse", version="1.0.0")

REQUESTS = Counter(
    "cloudpulse_http_requests_total",
    "Total HTTP requests handled",
    ["method"],
)

@app.middleware("http")
async def track_requests(request: Request, call_next):
    response = await call_next(request)
    REQUESTS.labels(method=request.method).inc()
    return response

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
    <html>
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>CloudPulse</title>
      <style>
        body { font: 18px Arial; background: #101827; color: white;
               max-width: 760px; margin: 60px auto; padding: 20px; }
        section { background: #1e293b; padding: 24px;
                  border-radius: 12px; margin-top: 20px; }
        a { color: #7dd3fc; margin-right: 12px; }
        .status { color: #4ade80; }
      </style>
    </head>
    <body>
      <h1>CloudPulse</h1>
      <p>DevOps Deployment & Observability Platform</p>
      <section>
        <h2>Application status</h2>
        <p class="status">● Application is running</p>
        <p>Dockerized application with automated CI/CD.</p>
      </section>
      <section>
        <h2>Endpoints</h2>
        <a href="/health">Health</a>
        <a href="/ready">Readiness</a>
        <a href="/metrics">Metrics</a>
        <a href="/docs">API Docs</a>
      </section>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.get("/metrics")
def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )
