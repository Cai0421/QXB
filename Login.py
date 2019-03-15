from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from Check import check
import time
###实现登陆的模块
### 解决登陆时候的相关问题
### 根据提供的URL进行登陆
class Login_user():
    def __init__(self,url,phone_number):
        self.url = url
        self.phone_number = phone_number
    def login(self):
        try:
            chrome_login = webdriver.Chrome(executable_path='/Add_Data/chromedriver.exe')
            #此处需要更改
            chrome_login.implicitly_wait(10)
            chrome_login.get(self.url)
            chrome_login.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[1]/input[@class="form-control input-lg input-flat"]').send_keys(phone_num)
            #密码
            chrome_login.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[2]/input[@class="form-control input-lg input-flat"]').send_keys(phone_passwd)
            #点击登录'/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[4]/a'
            chrome_login.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[4]/a[@class="btn btn-primary btn-block btn-lg"]').click()

            #获取页面
            init_page = chrome_login.page_source
            ## 返回账号密码错误时,重新执行登陆操作
            chrome_login.close()
            self.login()
            ## 返回账号异常时，停止一段时间然后
            time.sleep(120)
            ## 验证码问题
            ## 点击 chrome_login.click()

            ### 此处要采用循环， 直到页面加载正常
            check_address = check(init_page)
            if check_address.type == 1:
                result_check = check_address.slide_check()
                #引用解决滑动验证的函数
            if check_address.type == 2:
                result_check = check_address.click_check()
                #引用解决点击验证的函数
            ## 1. 返回正常页面
            ## 2. 验证内容
        except WebDriverException as e:
            print(e)
            info_fail = 'fail'
            return info_fail
        finally:
            try:
                chrome_login.close()
            except Exception:
                info_none = 'weizhi'
                return info_none
    ## 可以将滑动验证，点击验证的返回函数放在此处分离
    ## 函数返回的值都为page
            
