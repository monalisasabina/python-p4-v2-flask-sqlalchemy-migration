"""rename department

Revision ID: 70511afce835
Revises: 7951cd4052ed
Create Date: 2024-10-02 18:11:37.272718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70511afce835'
down_revision = '7951cd4052ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
