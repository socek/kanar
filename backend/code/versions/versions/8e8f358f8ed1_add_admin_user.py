"""add admin user

Revision ID: 8e8f358f8ed1
Revises: b889c5adfefd
Create Date: 2017-07-26 08:21:29.038652

"""
import sqlalchemy as sa

from alembic import op
from bcrypt import gensalt
from bcrypt import hashpw


# revision identifiers, used by Alembic.
revision = '8e8f358f8ed1'
down_revision = 'b889c5adfefd'
branch_labels = None
depends_on = None

user_table = sa.sql.table(
    'users',
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('name', sa.String(50), nullable=False),
    sa.Column('password', sa.String(100), nullable=True))


def hash_password(password):
    pwhash = hashpw(password.encode('utf8'), gensalt())
    return pwhash.decode('utf8')


def upgrade():
    op.bulk_insert(
        user_table,
        [
            {
                'name': 'admin',
                'password': hash_password('admin')
            },
        ]
    )


def downgrade():
    pass
