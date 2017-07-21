"""create user table

Revision ID: 2345e7af91cb
Revises:
Create Date: 2017-07-21 12:04:16.490117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2345e7af91cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )


def downgrade():
    pass
