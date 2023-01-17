import mongoengine
from src.configs import MongoDBConfigs

mongoengine.connection.connect(
    host=MongoDBConfigs.db_url,
    db=MongoDBConfigs.db_name,
)