import os
from sqlalchemy import MetaData,create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker



engine = create_engine('mysql+mysqldb://' + os.environ['DB_ID']+":"+os.environ['DB_PASSWORD']+"@"+os.environ['DB_IP_ADDRESS']+'/db_creedit', convert_unicode=True, echo=True)

metadata=MetaData()
metadata.reflect(engine,only=['stat','categorymap','channels','statistics'])
#metadata.reflect(engine,only=['stat','categorymap','channels'])
Base=automap_base(metadata=metadata)
Base.prepare()

session=sessionmaker(bind=engine)
s=session()
#testrebase