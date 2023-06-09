"""empty message

Revision ID: e120d40234a4
Revises: c1ca3c0ace3c
Create Date: 2023-05-29 20:22:26.173855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e120d40234a4'
down_revision = 'c1ca3c0ace3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cars', schema=None) as batch_op:
        batch_op.alter_column('color',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cars', schema=None) as batch_op:
        batch_op.alter_column('color',
               existing_type=sa.String(length=100),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
