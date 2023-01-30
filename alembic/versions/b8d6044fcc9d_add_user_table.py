"""add user table

Revision ID: b8d6044fcc9d
Revises: e9ba0a4ba0df
Create Date: 2023-01-23 21:19:34.329419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8d6044fcc9d'
down_revision = 'e9ba0a4ba0df'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False),
                            sa.Column('email', sa.String(), nullable=False),
                            sa.Column('password', sa.String(), nullable=False),
                            sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False),
                            sa.PrimaryKeyConstraint('id'),
                            sa.UniqueConstraint('email')

    )
    pass


def downgrade():
    op.drop_table('users')
    pass
