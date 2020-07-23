from sqlalchemy import MetaData,create_engine
from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session,session

##using declartive base###############
#Base = declarative_base()

#engine = create_engine('mysql+mysqldb://ehdgus93:ehdgus93!@203.245.30.13:3306/db_creedit_new', convert_unicode=True, echo=True)
#session = sessionmaker(bind=engine)
#session.configure(bind=engine)
#Base.metadata.create_all(engine)

#s = session()
######################################

##automap with some tables we want look at.###############
engine = create_engine('mysql+mysqldb://ehdgus93:ehdgus93!@203.245.30.13:3306/db_creedit_new', convert_unicode=True, echo=True)

metadata=MetaData()
metadata.reflect(engine,only=['stat','categorymap','channels','statistics'])
Base=automap_base(metadata=metadata)
Base.prepare()

session=sessionmaker(bind=engine)
s=session()

#query example
#query=s.query(Categorymap.cid,Categorymap.category_id)
#for cid,category_id in query:
#    print(cid,category_id)
###########################################################


##automap with whole table##################################
#Base=automap_base()
#engine = create_engine('mysql+mysqldb://ehdgus93:ehdgus93!@203.245.30.13:3306/db_creedit_new', convert_unicode=True, echo=True)
#Base.prepare(engine,reflect=True)

#Stat=Base.classes.stat
#Categorymap=Base.classes.categorymap
#Channels=Base.classes.channels

#session=sessionmaker(bind=engine)
#s=session()

#query=s.query(Categorymap.cid,Categorymap.category_id)
#for cid,category_id in query:
#    print(cid,category_id)
########################################################