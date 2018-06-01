from pymongo import MongoClient

from bson.objectid import ObjectId
import threading


# 通訊類型
# from enum import Enum, IntEnum, unique
#
# try:
#     @unique
#     class OPERATION(Enum):
#         MSG = 0
#         NUMCHANGE = 1
#         ISALIVE = 2
#         CONNECT = 3
#         CHANGEPWD = 4
#         PWDCHANGE = 5
#         LOGIN = 6
# except ValueError as e:
#     print(e)
#
# spliteTag = '$@~&*^$'


class DataBaseChatRoom():
    def __init__(self):
        self.client = MongoClient('localhost', 27017)  # 比较常用
        self.database = self.client["chatroom"]  # SQL: Database Name
        self.collection = self.database["account"]  # SQL: Table Name
        print("connect OK")


    def loadData(self):#server讀取資料
        #print(self.collection.find().count())
        userList = []
        for ii in self.collection.find().sort('uname'):
            userList.append({'uname': self.uname, 'upwd': self.upwd})
        print("load OK")
        return None

    # delete user by uname
    # dbChatRoom.deleteUser(['A'])
    def deleteUser(self, unameList=None):
        self.collection.delete_many({'uname':unameList})
        return 'successful'

    # insert user
    # dbChatRoom.insertUser(uname='A', upwd='A')
    def insertUser(self, uname=None, upwd=None):#server新增資料
        self.collection.insert_one({'uname': uname, 'upwd': upwd})
        return 'successful'

    def updataUser(self, uname=None, upwd=None):
        temp = self.collection.find_one({'uname' : uname})
        temp['upwd'] = upwd
        temp2 = temp.copy()
        self.collection.update(temp, temp2)
        return 'successful'

    # check checkUserExist
    def checkUserExist(self, uname='A'):
        pass
        return False

    # query user bu uname
    # dbChatRoom.queryByuname(uname='A', upwd='A')
    def queryByuname(self, uname='A', upwd='A'):
        pass
        return False

    # Init database
    # dbChatRoom.Initdatabase()
    def Initdatabase(self):
        userList = []
        #userList.append({'uname': 'A', 'upwd': '1'})
        #userList.append({'uname': 'B', 'upwd': '2'})
        #self.collection.insert_many(userList)

    def colseClient(self):
        self.client.close()


def main():
    dbChatRoom = DataBaseChatRoom()
    dbChatRoom.Initdatabase()
    dbChatRoom.colseClient()


if __name__ == "__main__":

    main()
