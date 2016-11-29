from __future__ import print_function

from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.core.cache import cache
from django.conf import settings
from typing import Any, Dict

import logging

def flush_cache(sender, **kwargs):
    # type: (AppConfig, **Any) -> None
    logging.info("Clearing memcached cache after migrations")
    cache.clear()


cla ss ZerverConfig(AppConfig):
    name = "zerver"  # type: str

    def ready(self):
        # type: () -> None
        if settings.POST_MIGRATION_CACHE_FLUSHING:
            post_migrate.connect(flush_cache, sender=self)
