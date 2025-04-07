from typing import Optional

import sqlalchemy as sa

engine = sa.create_engine("sqlite:///:memory:") 
connection = engine.connect() 

metadata = sa.MetaData() 

user_table = sa.Table(
    "user",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("firstname",sa.String),
    sa.Column("lastname",sa.String),
    sa.Column("email",sa.String),
    sa.Column("latitude",sa.Float),
    sa.Column("longitude",sa.Float)
)


def insert_user(firstname: str, lastname:str, email: str, latitude: float, longitude: float) -> None:
    query = user_table.insert().values(firstname=firstname, lastname=lastname, email= email, latitude=latitude, longitude=longitude)
    connection.execute(query)

def get_user(userid: int) -> Optional[dict]:
    query = user_table.select().where(user_table.c.id == userid)
    result = connection.execute(query)
    return result.fetchone() 

def save_to_db(users: list) -> None:
    metadata.create_all(engine) 
    for user in users:
        insert_user(user['firstName'], user['lastName'], user['email'], user['address']['coordinates']['lat'], user['address']['coordinates']['lng'])
    

# def main()-> None:     
#     metadata.create_all(engine)
