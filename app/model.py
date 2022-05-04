import pymysql.cursors
import rds_config as RDS

def question_info():
    connect = pymysql.connect(host= RDS.rds_host,
                            user= RDS.db_user,
                            password= RDS.db_password,
                            db= RDS.db_name,
                            charset='utf8mb4',
                            port = 3306,
                            cursorclass=pymysql.cursors.DictCursor)

    with connect.cursor() as cursor:
        sql = "SELECT * FROM question_lists"
        cursor.execute(sql)
        results = cursor.fetchall()

    connect.close()
    return results