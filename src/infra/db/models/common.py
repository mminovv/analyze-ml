import uuid

import sqlalchemy as sa
from sqlalchemy import (
    DateTime,
    MetaData,
    func,
)
from sqlalchemy.dialects import postgresql as psql
from sqlalchemy.orm import as_declarative
from sqlalchemy.orm.attributes import set_attribute


class SoftDeleteMixin:
    deleted_at = sa.Column(
        DateTime,
        nullable=True,
    )

    def delete(self):
        self.deleted_at = func.now()


@as_declarative()
class Base:
    metadata: MetaData

    id = sa.Column(
        psql.UUID(as_uuid=True),
        default=uuid.uuid4,
        primary_key=True,
        index=True,
    )
    created_at = sa.Column(
        DateTime,
        server_default=func.now(),
    )
    updated_at = sa.Column(
        DateTime,
    )

    def update(self, **kwargs):
        """Update instance attributes and bump last_modified date in stats"""
        for key, value in kwargs.items():
            set_attribute(self, key, value)
