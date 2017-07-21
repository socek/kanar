"""Add password

Revision ID: b889c5adfefd
Revises: 2345e7af91cb
Create Date: 2017-07-21 13:32:42.770471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b889c5adfefd'
down_revision = '2345e7af91cb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'users',
        sa.Column('password', sa.String(100), nullable=True))


def downgrade():
    pass
