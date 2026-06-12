from sqlalchemy import Column, String, Numeric, DateTime
from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.database import Base
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)


class Account(Base):
    __tablename__ = "accounts"

    account_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    account_number = Column(
        String,
        unique=True,
        nullable=False
    )

    customer_name = Column(
        String,
        nullable=False
    )

    balance = Column(
        Numeric(12, 2),
        default=0.00
    )

    status = Column(
        String,
        default="ACTIVE"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    account_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )

    transaction_type = Column(
        String,
        nullable=False
    )

    amount = Column(
        Numeric(12, 2),
        nullable=False
    )

    status = Column(
        String,
        default="SUCCESS"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

class AuditEvent(Base):
    __tablename__ = "audit_events"

    id = Column(Integer, primary_key=True, index=True)

    event_id = Column(String, unique=True, nullable=False)

    event_type = Column(String, nullable=False)

    status = Column(String, nullable=False)

    details = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)