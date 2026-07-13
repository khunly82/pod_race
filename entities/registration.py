from entities import Base
from sqlalchemy import Column, ForeignKey, Table

registration = Table(
    'registrations', 
    Base.metadata, 
    Column('race_id', ForeignKey('races.id')), 
    Column('pilot_id', ForeignKey('pilots.id'))
)