"""empty message

Revision ID: 47f6d03c3337
Revises: b66541c236c1
Create Date: 2019-05-28 10:39:55.912890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47f6d03c3337'
down_revision = 'b66541c236c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('birthday', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'birthday')
    # ### end Alembic commands ###