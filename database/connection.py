from pymysql import *
class connections:
    def ConnectMe(self):
        con = connect("127.0.0.1", "root", "", "healthfit")
        return con