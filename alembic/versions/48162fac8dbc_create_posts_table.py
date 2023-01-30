"""create posts table

Revision ID: 48162fac8dbc
Revises: 
Create Date: 2023-01-23 20:52:23.270326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48162fac8dbc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass