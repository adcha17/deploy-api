from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/var/www/python/deploy_api_vmc/gunicorn.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/var/www/python/deploy_api_vmc/access_log.log'
errorlog =  '/var/www/python/deploy_api_vmc/error_log.log'

# Timeout
timeout = 99999
