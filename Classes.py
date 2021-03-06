import _md5
import hashlib
class User:
    id = None
    username = None
    password = None
    reputation = None
    firstname = None
    lastname = None

    def login(self, database, cursor, login, password):
        login_sql = "SELECT * FROM users WHERE username = ? AND password = ?"
        hashpassword = hashlib.md5(bytes(password.encode()))
        login_sql_param = (login, hashpassword.hexdigest())
        cursor.execute(login_sql, login_sql_param)
        str = cursor.fetchall()
        boolforret = False
        if not len(str) < 1:
            self.id = str[0][0]
            self.username = str[0][1]
            self.password = str[0][2]
            self.reputation = str[0][3]
            self.firstname = str[0][4]
            self.lastname = str[0][5]
            boolforret = True
        forret = [self, boolforret]
        return forret

    def register(self, database, cursor, login, password, firstname, lastname):
        reg_sql = "INSERT INTO users (id, username, password, reputation, firstname, lastname, cmdAccAndRej) VALUES (NULL, ?, ?, 100, ?, ?, 0)"
        hashpassword = hashlib.md5(bytes(password.encode()))
        reg_sql_param = (login, hashpassword.hexdigest(), firstname, lastname)
        cursor.execute(reg_sql, reg_sql_param)
        self.firstname = firstname
        self.lastname = lastname
        self.username = login
        self.password = password
        self.reputation = 100
        database.commit()
        pass
        
    def GetArtAcRePern(self, database, cursor, user):
        GetArtAcRePern_sql = "SELECT cmdAccAndRej from users WHERE ID = ?"
        GetArtAcRePern_sql_params = (str(user.id),)
        cursor.execute(GetArtAcRePern_sql, GetArtAcRePern_sql_params)
        strka = cursor.fetchone()
        return strka

    def getRepu(self, database, cursor, user):
        GetArtAcRePern_sql = "SELECT reputation from users WHERE ID = ?"
        GetArtAcRePern_sql_params = (str(user.id),)
        cursor.execute(GetArtAcRePern_sql, GetArtAcRePern_sql_params)
        strka = cursor.fetchone()
        return strka
       
      
class Article:
    id = None
    title = None
    desc = None
    byUserID = None
    imgPath = None
    def fetchById(self, id, database, cursor):
        fetchbyId_sql = "SELECT * from articles WHERE id = ?"
        fetchbyId_sql_params = (id,)
        cursor.execute(fetchbyId_sql, fetchbyId_sql_params)
        str = cursor.fetchall()
        print (str)
        self.id = str[0][0]
        self.title = str[0][1]
        self.desc = str[0][2]
        self.byUserID = str[0][3]
        self.imgPath = str[0][5]
        return self

    def newArticle(self, name, desc, database, user, cursor, path):
        newArticleSQL = "INSERT INTO articles (id, title, desc, byUserid, isAccepted, imgPath) VALUES (NULL, ?, ?, ?, 0, ?)"
        newArticleSQL_params = (name, desc, user.id, path)
        cursor.execute(newArticleSQL, newArticleSQL_params)
        database.commit()
        pass
        
    def accept(self, database, cursor):
        acceptSQL = "UPDATE articles SET isAccepted=? WHERE id = ?"
        acceptSQL_Par = (1, self.id)  
        cursor.execute(acceptSQL, acceptSQL_Par)
        database.commit()
        pass
        
    def reject(self, database, cursor):
        acceptSQL = "UPDATE articles SET isAccepted=? WHERE id = ?"
        acceptSQL_Par = (-1, self.id)
        cursor.execute(acceptSQL, acceptSQL_Par)
        database.commit()
        pass
       
    def getStatus(self, database, cursor):
        getStatus_sql = "SELECT isAccepted from articles WHERE id = ?"
        getStatus_sql_params = (self.id,)
        cursor.execute(getStatus_sql, getStatus_sql_params)
        str = cursor.fetchone()
        return str[0]

    def getLastID(self, database, cursor):
        getLastID_sql = "SELECT id FROM articles ORDER BY id DESC LIMIT 0, 49999;"
        cursor.execute(getLastID_sql)
        id = cursor.fetchone()[0]
        return id

"""SELECT "_rowid_",* FROM "main"."articles"  ORDER BY "id" DESC LIMIT 0, 49999;"""