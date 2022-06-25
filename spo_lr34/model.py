from peewee import *
import psycopg2

db = PostgresqlDatabase('spo', user='postgres', password='admin')


class BaseModel(Model):
    class Meta:
        database = db


class Types(BaseModel):
    type_name = TextField(null=True)
    source_name = TextField(null=True)
    target_name = TextField(null=True)


class Terms(BaseModel):
    xml_id = IntegerField()
    value = CharField(null=True)
    description = TextField(null=True)
    style = TextField(null=True)


class Links(BaseModel):
    source = ForeignKeyField(Terms, null=True)
    target = ForeignKeyField(Terms, null=True)
    link_type_id = ForeignKeyField(Types, null=True)
    value_arrow = CharField(null=True)


def connect_db():
    db.connection()
    db.drop_tables([Terms, Types, Links])
    db.create_tables([Terms, Types, Links])


def close_db():
    db.close()


def create_types():
    data_source = [
        {'type_name': 'Выполняет', 'source_name': 'Выполняет', 'target_name': 'Выполняется'},
        {'type_name': 'Причина-следствие', 'source_name': 'Причина для', 'target_name': 'Следствие для'},
        {'type_name': 'Инструмент', 'source_name': 'Использует', 'target_name': 'Инструмент для'}
    ]

    Types.insert_many(data_source).execute()
