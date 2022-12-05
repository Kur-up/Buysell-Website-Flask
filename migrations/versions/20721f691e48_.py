"""empty message

Revision ID: 20721f691e48
Revises: e5a9e6dc9972
Create Date: 2022-12-05 13:15:58.875131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20721f691e48'
down_revision = 'e5a9e6dc9972'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone_number', sa.String(length=32), nullable=True))
        batch_op.add_column(sa.Column('registration_timestamp', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('visiting_timestamp', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('rating', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('banned', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('sending_recommendations', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('sending_messages', sa.Boolean(), nullable=True))
        batch_op.create_index(batch_op.f('ix_user_model_phone_number'), ['phone_number'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_model', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_model_phone_number'))
        batch_op.drop_column('sending_messages')
        batch_op.drop_column('sending_recommendations')
        batch_op.drop_column('banned')
        batch_op.drop_column('rating')
        batch_op.drop_column('visiting_timestamp')
        batch_op.drop_column('registration_timestamp')
        batch_op.drop_column('phone_number')

    # ### end Alembic commands ###