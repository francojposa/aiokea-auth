import sqlalchemy as sa
from sqlalchemy import ForeignKey

METADATA = sa.MetaData()

AUTH_USER = sa.Table(
    "auth_user",
    METADATA,
    sa.Column("id", sa.String, primary_key=True),
    sa.Column("username", sa.String, unique=True, nullable=False),
    sa.Column("email", sa.String, unique=True, nullable=False),
    sa.Column("password", sa.String, nullable=False),
    sa.Column("is_enabled", sa.Boolean, nullable=False, server_default="true"),
    sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
    sa.Column(
        "updated_at",
        sa.DateTime,
        nullable=False,
        server_default=sa.func.now(),
        server_onupdate=sa.func.now(),
    ),
)

AUTH_ROLE = sa.Table(
    "auth_role",
    METADATA,
    sa.Column("id", sa.String, primary_key=True),
    sa.Column("role", sa.String, unique=True, nullable=False),
    sa.Column("is_enabled", sa.Boolean, nullable=False, server_default="true"),
    sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
    sa.Column(
        "updated_at",
        sa.DateTime,
        nullable=False,
        server_default=sa.func.now(),
        server_onupdate=sa.func.now(),
    ),
)

AUTH_USER_ROLE = sa.Table(
    "auth_user_role",
    METADATA,
    sa.Column("id", sa.String, primary_key=True),
    sa.Column(
        "user_id",
        sa.String,
        ForeignKey("auth_user.id", onupdate="CASCADE", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    ),
    sa.Column(
        "role_id",
        sa.String,
        ForeignKey("auth_role.id", onupdate="CASCADE", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    ),
)
