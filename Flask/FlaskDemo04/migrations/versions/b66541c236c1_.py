"""empty message

Revision ID: b66541c236c1
Revises: 8d5cf32c8572
Create Date: 2019-05-27 17:51:11.448330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b66541c236c1'
down_revision = '8d5cf32c8572'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wife', sa.Column('birthday', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('wife', 'birthday')
    # ### end Alembic commands ###
