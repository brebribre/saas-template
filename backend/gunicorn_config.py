# gunicorn_config.py

# Worker configuration
workers = 2  # Reduced number of workers for Digital Ocean's resource constraints
worker_class = 'uvicorn.workers.UvicornWorker'  # Using Uvicorn workers for ASGI
threads = 1  # Single thread per worker

# Request handling
max_requests = 1000
max_requests_jitter = 50
timeout = 29  # Keep under 30 seconds for Digital Ocean's health check
graceful_timeout = 29
keepalive = 2

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Process naming
proc_name = 'backend'

# Bind - Let Digital Ocean handle the port binding
bind = '0.0.0.0:8080'

# SSL (uncomment if using HTTPS)
# keyfile = 'path/to/keyfile'
# certfile = 'path/to/certfile'

# Prevent timeouts during startup
timeout = 0  # During startup
preload_app = True  # Load application code before worker processes are forked
