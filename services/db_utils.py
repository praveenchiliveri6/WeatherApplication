import yaml
from yaml.loader import SafeLoader
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sql
import sqlalchemy.ext.declarative as sqldcl
from sqlalchemy import Column,String,Integer


class DBUtils:

    def __init__(self):
        global properties
        with open('./properties.yaml') as f:
            properties = yaml.load(f, Loader=SafeLoader)

    def connect_to_db(self):
        logger_db_props = properties['DataBase']
        host = logger_db_props.get("host")
        port = logger_db_props.get("port")
        database = logger_db_props.get("database")
        user = logger_db_props.get("user")
        password = logger_db_props.get('password')

        DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

        try:
            engine = sql.create_engine(DATABASE_URI)
            return engine
        except Exception as err:
            raise Exception(err)

    def add_city_to_db(self,engine,schema_name,table_name,new_city_name):
        try:
            Session = sessionmaker(bind=engine)
            session=Session()
            Base = sqldcl.declarative_base(metadata=sql.MetaData(engine,schema=schema_name))

            class City(Base):
                __tablename__ = table_name
                id = Column(Integer,primary_key=True)
                city_name = Column(String)

            new_city_info = City(city_name=new_city_name)

            try:
                session.add(new_city_info)
                session.commit()
            except Exception as error:
                session.rollback()
                print("Failed to insert the new city into table. Error - {}".format(error))
        except Exception as error:
            print("Error - {}".format(error))

    def fetch_all_cities(self,engine,schema_name,table_name):

        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            Base = sqldcl.declarative_base(metadata=sql.MetaData(engine,schema=schema_name))

            class City(Base):
                __tablename__ = table_name
                id = Column(Integer,primary_key=True)
                city_name = Column(String)

            query_response = session.query(City)
            return query_response

        except Exception as error:
            print("Failed to fetch cities from database table. Error - {}".format(error))
            return []
