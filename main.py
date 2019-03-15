import Range
import cookies
from GetUrl import get_url
from Login import Login_user

if __name__ == "__main__":
    ## 循环
    first_grade = ''
    second_grade = ''
    regin_id = 40013
    condition = [first_grade,second_grade]
    url_collect = get_url(regin_id,condition)
    url_all = url_collect.url_()

    ### 爬取数据并保存数据，该处可以采用多线程
        
    
