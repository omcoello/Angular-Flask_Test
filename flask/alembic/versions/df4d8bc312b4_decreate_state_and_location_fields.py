"""DeCreate state and location fields

Revision ID: df4d8bc312b4
Revises: d31be22baf0a
Create Date: 2024-03-17 20:39:03.449200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df4d8bc312b4'
down_revision: Union[str, None] = 'd31be22baf0a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('state', sa.String(length=50), nullable=True))
    op.add_column('account', sa.Column('location', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('account', 'location')
    op.drop_column('account', 'state')
    # ### end Alembic commands ###
