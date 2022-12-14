"""empty message

Revision ID: 63c4d54f50f8
Revises: b334e4d81458
Create Date: 2022-12-07 13:50:00.091049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63c4d54f50f8'
down_revision = 'b334e4d81458'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personal_items_accessories_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('photo_list', sa.PickleType(), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('create_timestamp', sa.DateTime(), nullable=True),
    sa.Column('stop_timestamp', sa.DateTime(), nullable=True),
    sa.Column('active_status', sa.Boolean(), nullable=True),
    sa.Column('deleted_status', sa.Boolean(), nullable=True),
    sa.Column('like_count', sa.Integer(), nullable=True),
    sa.Column('clothes_type', sa.String(length=32), nullable=True),
    sa.Column('clothes_sex', sa.String(length=16), nullable=True),
    sa.Column('clothes_status', sa.String(length=16), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city_model.id'], ),
    sa.ForeignKeyConstraint(['country_id'], ['country_model.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['user_model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('personal_items_accessories_model', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_personal_items_accessories_model_title'), ['title'], unique=False)

    op.create_table('personal_items_shoes_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('photo_list', sa.PickleType(), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('create_timestamp', sa.DateTime(), nullable=True),
    sa.Column('stop_timestamp', sa.DateTime(), nullable=True),
    sa.Column('active_status', sa.Boolean(), nullable=True),
    sa.Column('deleted_status', sa.Boolean(), nullable=True),
    sa.Column('like_count', sa.Integer(), nullable=True),
    sa.Column('clothes_season', sa.String(length=32), nullable=True),
    sa.Column('clothes_sex', sa.String(length=16), nullable=True),
    sa.Column('clothes_size', sa.String(length=8), nullable=True),
    sa.Column('clothes_status', sa.String(length=16), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city_model.id'], ),
    sa.ForeignKeyConstraint(['country_id'], ['country_model.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['user_model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('personal_items_shoes_model', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_personal_items_shoes_model_title'), ['title'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('personal_items_shoes_model', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_personal_items_shoes_model_title'))

    op.drop_table('personal_items_shoes_model')
    with op.batch_alter_table('personal_items_accessories_model', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_personal_items_accessories_model_title'))

    op.drop_table('personal_items_accessories_model')
    # ### end Alembic commands ###
