### 验证码的问题

# 返回验证码类型
def judge_type(check_page):
    _type = 0
    return _type
class check():
    def __init__(self, check_page):
        #控制验证码类型
        self.type = 0
        #验证码页面
        self.check_page = check_page
        self.type = judge_type(self.check_page)
    ## 滑动验证码
    def slide_check(self):
        result = []
        return [self.type, result]
    ## 点击验证码
    def click_check(self):
        result = []
        return [self.type, result]


