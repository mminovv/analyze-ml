from dishka.integrations.arq import (
    job_end, # noqa
    job_start, # noqa
)


class _WorkerSettings:
    on_job_start = job_start(None)
    on_job_end = job_end(None)
    functions = []
    cron_jobs = []
    redis_settings = ...
