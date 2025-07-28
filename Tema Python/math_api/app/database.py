
import oracledb

USERNAME = "STAGING"
PASSWORD = "qwertyuiop"
DSN = "localhost:1521/ORCLPDB1"  # ex: "localhost/orclpdb1" sau ce ai deja testat

connection = oracledb.connect(
    user=USERNAME,
    password=PASSWORD,
    dsn=DSN
)