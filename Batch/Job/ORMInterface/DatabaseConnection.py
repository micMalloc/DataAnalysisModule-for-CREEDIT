from sqlalchemy import MetaData,create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#Base = declarative_base()

#engine = create_engine('mysql+mysqldb://ehdgus93:ehdgus93!@203.245.30.13:3306/db_creedit_new', convert_unicode=True, echo=True)
#session = sessionmaker(bind=engine)
#session.configure(bind=engine)
#Base.metadata.create_all(engine)

#s = session()

engine = create_engine('mysql+mysqldb://ehdgus93:ehdgus93!@203.245.30.13:3306/db_creedit_new', convert_unicode=True, echo=True)
session = sessionmaker(bind=engine)
s=session()


metadata=MetaData()
metadata.reflect(engine)
Base=automap_base(metadata=metadata)
Base.prepare(engine,reflect=True)
