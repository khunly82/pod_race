"""Seeds

Revision ID: 13419a74e09c
Revises: 49521d64e350
Create Date: 2026-07-08 15:27:14.101370

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13419a74e09c'
down_revision: Union[str, Sequence[str], None] = '49521d64e350'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Insert seed data."""
    
    # Insert Pilots
    pilots_table = sa.table(
        'pilots',
        sa.column('id', sa.Integer),
        sa.column('name', sa.String),
        sa.column('species', sa.String),
        sa.column('credits', sa.Integer),
        sa.column('status', sa.String),
        sa.column('level', sa.String),
    )
    
    op.bulk_insert(pilots_table, [
        {
            'id': 1,
            'name': 'Anakin Skywalker',
            'species': 'Humain',
            'credits': 1000,
            'status': 'active',
            'level': 'beginer',
        },
        {
            'id': 2,
            'name': 'Gasgano',
            'species': 'Xexto',
            'credits': 1000,
            'status': 'active',
            'level': 'beginer',
        },
        {
            'id': 3,
            'name': 'Ben Quadinaros',
            'species': 'Toong',
            'credits': 1000,
            'status': 'active',
            'level': 'beginer',
        },
        {
            'id': 4,
            'name': 'Sebulba',
            'species': 'Dug',
            'credits': 5000,
            'status': 'active',
            'level': 'legend',
        },
    ])
    
    # Insert Pods
    pods_table = sa.table(
        'pods',
        sa.column('id', sa.Integer),
        sa.column('name', sa.String),
        sa.column('base_speed', sa.Integer),
        sa.column('base_handling', sa.Integer),
        sa.column('shield', sa.Integer),
        sa.column('pilot_id', sa.Integer),
    )
    
    op.bulk_insert(pods_table, [
        {
            'id': 1,
            'name': 'Radon-Ulzer',
            'base_speed': 50,
            'base_handling': 40,
            'shield': 15,
            'pilot_id': 1,
        },
        {
            'id': 2,
            'name': 'Ord Pedrovia',
            'base_speed': 45,
            'base_handling': 55,
            'shield': 20,
            'pilot_id': 2,
        },
        {
            'id': 3,
            'name': 'Balta-Tridura',
            'base_speed': 30,
            'base_handling': 30,
            'shield': 10,
            'pilot_id': 3,
        },
        {
            'id': 4,
            'name': 'Plug-Gargantu',
            'base_speed': 70,
            'base_handling': 35,
            'shield': 35,
            'pilot_id': 4,
        },
    ])
    
    # Insert Parts
    parts_table = sa.table(
        'parts',
        sa.column('id', sa.Integer),
        sa.column('name', sa.String),
        sa.column('type', sa.String),
        sa.column('boost_speed', sa.Integer),
        sa.column('boost_handling', sa.Integer),
        sa.column('price', sa.Integer),
        sa.column('pod_id', sa.Integer),
    )
    
    op.bulk_insert(parts_table, [
        {
            'id': 1,
            'name': 'Injecteur d\'Hydro-Spanner',
            'type': 'engine',
            'boost_speed': 15,
            'boost_handling': 0,
            'price': 350,
            'pod_id': 1,
        },
        {
            'id': 2,
            'name': 'Lance-Flammes Illégal',
            'type': 'cockpit',
            'boost_speed': 0,
            'boost_handling': 0,
            'price': 600,
            'pod_id': 4,
        },
        {
            'id': 3,
            'name': 'Propulseur Kessel X-2',
            'type': 'thruster',
            'boost_speed': 25,
            'boost_handling': -5,
            'price': 450,
            'pod_id': None,
        },
        {
            'id': 4,
            'name': 'Stabilisateur Corellien',
            'type': 'cockpit',
            'boost_speed': 0,
            'boost_handling': 20,
            'price': 300,
            'pod_id': None,
        },
        {
            'id': 5,
            'name': 'Micro-Turbo à Plasma',
            'type': 'engine',
            'boost_speed': 35,
            'boost_handling': -10,
            'price': 800,
            'pod_id': None,
        },
        {
            'id': 6,
            'name': 'Blindage en Beskar Recyclé',
            'type': 'cockpit',
            'boost_speed': -5,
            'boost_handling': 5,
            'price': 500,
            'pod_id': None,
        },
    ])

    # op.execute("SELECT setval(pg_get_serial_sequence('pilots', 'id'), COALESCE(max(id), 0)) FROM pilots;")
    # op.execute("SELECT setval(pg_get_serial_sequence('pods', 'id'), COALESCE(max(id), 0)) FROM pods;")
    # op.execute("SELECT setval(pg_get_serial_sequence('parts', 'id'), COALESCE(max(id), 0)) FROM parts;")


def downgrade() -> None:
    """Remove seed data."""
    op.execute(sa.text('DELETE FROM parts'))
    op.execute(sa.text('DELETE FROM pods'))
    op.execute(sa.text('DELETE FROM pilots'))
