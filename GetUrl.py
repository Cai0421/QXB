from Login import Login_user
import  cookies
##该模块实现的内容
###1.根据所选的条件给出url regin_id , 
###2.condition 为first_grade, second_grade
###3. url_ 判断该行业下的数目多少，大于5000时进一步分类，返回url, 利用同一个账户
class get_url():
    def __init__(self, regin_id, condition):
        self.regin_id = regin_id
        self.condition = condition
        self.url = []
        self.number = 0
    
    def url_(self):
        url_login = 'http://'
        url_user = Login_user(cookies.user_account[0], url_login)
        # ....
        return {self.number, self.url}
