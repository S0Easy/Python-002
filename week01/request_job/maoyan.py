import requests
from bs4 import BeautifulSoup as  bs
import pandas as pd

url = "https://maoyan.com/films?showType=3"

def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    Cookie = '__mta=48602777.1596169299532.1596276128658.1596285970977.12; uuid_n_v=v1; uuid=210D6090D2E511EA85E7A5AA0F3C5F94C87407EE13C2457EB521404B679E1C74; mojo-uuid=7f1d4404924a2564c330da82dcc8c54b; _lxsdk_cuid=173a31a7732c8-079d06a4b7148b-3323765-151800-173a31a7733c8; _lxsdk=210D6090D2E511EA85E7A5AA0F3C5F94C87407EE13C2457EB521404B679E1C74; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _csrf=bd08d1dd2f7efc2bb3c901793aabd4a5c16753dcde843be07f3c4ba0cbdaa9a5; mojo-session-id={"id":"508adfed5e12f863a222f82f77b21e00","time":1596375090580}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1596170266,1596172000,1596248928,1596375095; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1596378492; mojo-trace-id=12; __mta=48602777.1596169299532.1596285970977.1596378492355.13; _lxsdk_s=173af5ee47e-ec8-501-c7%7C%7C20'

    header = {
                'user-agent': user_agent,
                'Cookie': Cookie
             }
    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text, 'html.parser')

    film_names = []
    film_types = []
    plan_dates = []
    for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'})[0:10]:
        for i, atag in enumerate(tags.find_all('div', attrs={'class': 'movie-hover-title'})):
            # print(i,": ",atag)
            if i == 0:
                film_name = atag.text.strip().split("\n")[0]
                film_names.append(film_name)
                print(f"电影名称: {film_name}")
            elif i == 1:
                film_type = atag.text.strip().split("\n")[1].strip()
                film_types.append(film_type)
                print(f"电影类型: {film_type}")
            elif i == 3:
                plan_date = atag.text.strip().split("\n")[1].strip()
                plan_dates.append(plan_date)
                print(f"上映日期: {plan_date}")
    file_csv = pd.DataFrame({'film_name': film_names, 'film_type': film_types, 'plan_date': plan_dates})
    file_csv.to_csv("./maoyan_movies.csv",index=False)


if __name__ == "__main__":
    get_url_name(url)