from tenant_schemas.models import TenantMixin
from django.db import connection
from metrics import logger

class CustomTenantMixin(TenantMixin):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        logger.debug(f"[CustomTenantMixin: save] Current schema: {connection.schema_name}")
        logger.debug(f"[CustomTenantMixin: save] Object schema: {self.schema_name}")
        logger.debug(f"[CustomTenantMixin: save] Is new object: {self.pk is None}")
        try:
            super().save(*args, **kwargs)
            logger.debug(f"[CustomTenantMixin: save] Save successful")
        except Exception as e:
            logger.error(f"[CustomTenantMixin: save] Save failed: {str(e)}")
            raise