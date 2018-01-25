# 下载王者荣耀全部英雄海报
# 海报尺寸可选，截至目前共计 242 张，1080P 大小约 160 MB
# author: By_syk <By_syk@163.com>
# date: 2018-01-25


from urllib import request
import json
import os
import urllib

# 英雄数据URL
# 核心参数：页次 page，每页数量 iListNum
URL_HERO = r'http://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?' \
           r'sDataType=JSON&iActId=2735&iListNum=64&page=%d'
# 图片存放路径
FOLDER_SAVE = r'E:/Download/QQPVPHeroCover/1920x1080'


def download_cover(url_img, hero_and_skin_name):
    if not os.path.exists(FOLDER_SAVE):
        os.makedirs(FOLDER_SAVE)

    name_arr = hero_and_skin_name.split('-')
    hero_name = name_arr[0]
    skin_name = name_arr[1]
    print('downloading:', hero_name, '-', skin_name, end=' ')
    file_path = '%s/%s-%s.jpg' % (FOLDER_SAVE, hero_name, skin_name)  # 生成图片文件名
    if os.path.exists(file_path):  # 避免重复下载
        print('[exists]')
        return
    # 样例：http://shp.qpic.cn/ishow/2735012211/1516590356_84828260_8310_sProdImgNo_6.jpg/0
    if url_img.endswith('/200'):  # 生成海报图片URL
        url_img = url_img[:-3] + '0'
    request.urlretrieve(url_img, file_path)
    print('[ok]')


def download_all():
    print('start to download')
    for i in range(0, 10):
        res = request.urlopen(URL_HERO % i)
        data = res.read().decode('utf-8')
        data_json = json.loads(data)
        # data['iTotalLines'] 总数
        core_json = data_json['List']
        if len(core_json) == 0:
            break
        for hero_data in core_json:
            # 壁纸尺寸参数：
            # sProdImgNo_2: 1024x768
            # sProdImgNo_3: 1280x720
            # sProdImgNo_4: 1280x1024
            # sProdImgNo_5: 1440x900
            # sProdImgNo_6: 1920x1080
            # sProdImgNo_7: 1920x1200
            # sProdImgNo_8: 1920x1440
            download_cover(urllib.request.unquote(hero_data['sProdImgNo_6']),
                           urllib.request.unquote(hero_data['sProdName']))
    print('all done')


if __name__ == '__main__':
    download_all()
