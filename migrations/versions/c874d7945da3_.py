"""empty message

Revision ID: c874d7945da3
Revises: a2d99b1d0ae1
Create Date: 2024-01-04 14:03:05.128923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c874d7945da3'
down_revision = 'a2d99b1d0ae1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bearbeiter', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_plan_bearbeiter', 'user', ['bearbeiter'], ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.drop_constraint('fk_plan_bearbeiter', type_='foreignkey')
        batch_op.drop_column('bearbeiter')

    # ### end Alembic commands ###
