"""updates

Revision ID: 92b6139bffb9
Revises: eea9ab1dc8ca
Create Date: 2022-08-17 22:41:44.484683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92b6139bffb9'
down_revision = 'eea9ab1dc8ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('test', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artist', 'test')
    # ### end Alembic commands ###
