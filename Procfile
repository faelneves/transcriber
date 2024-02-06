web: gunicorn main:app \
 --log-file . \
 --log-level debug \
 --timeout 600 \
 --workers 1 \
 --worker-class uvicorn.workers.UvicornWorker