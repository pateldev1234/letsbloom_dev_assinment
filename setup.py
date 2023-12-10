import pymysql
import config

mysql_connector = pymysql.connect(
    host = config.DB_HOST,
    user = config.DB_USERNAME,
    database = config.DB_DATABASE_NAME,
    passwd = config.DB_PASSWORD
)

mysql_connector_cursor = mysql_connector.cursor()
