"""add content column to posts table

Revision ID: e9ba0a4ba0df
Revises: 48162fac8dbc
Create Date: 2023-01-23 21:05:41.365960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9ba0a4ba0df'
down_revision = '48162fac8dbc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
