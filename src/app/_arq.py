import logging

from arq import cron
from arq.connections import RedisSettings
from dishka.integrations.arq import setup_dishka

from src.core.settings import settings
from src.infra.arq.settings import _WorkerSettings as WorkerSettings  # noqa
from src.infra.di.container import get_arq_container

logger = logging.getLogger(__name__)


def health_check():
    logger.info('Health check: OK')


def init_arq_worker(worker: WorkerSettings):
    redis_settings = RedisSettings(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        database=settings.REDIS_DB,

    )
    jobs = [
        cron(health_check, second=1)  # noqa
    ]
    worker.cron_jobs.extend(jobs)
    worker.redis_settings = redis_settings

    container = get_arq_container()
    setup_dishka(container=container, worker_settings=worker)  # noqa

    return worker


init_arq_worker(WorkerSettings)  # noqa
