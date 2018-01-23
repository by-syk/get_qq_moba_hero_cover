# 下载王者荣耀全部英雄海报
# 海报尺寸为 1920x882，截至目前共计 237 张，大小约 60 MB
# author: By_syk <By_syk@163.com>
# date: 2018-01-13


from urllib import request
import json
import os


# 英雄数据URL
URL_HERO = r'https://pvp.qq.com/web201605/js/herolist.json'
# 英雄海报图片URL
URL_HERO_COVER_IMG = r'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/%d/%d-bigskin-%d.jpg'
# 图片存放路径
FOLDER_SAVE = r'E:/Download/QQPVPHeroCover/'


def download_cover(hero_id, hero_name, cover_names):
    if not os.path.exists(FOLDER_SAVE):
        os.makedirs(FOLDER_SAVE)

    for i, cover_name in enumerate(cover_names):
        print('downloading:', hero_name, '-', cover_name, end=' ')
        file_path = '%s%s-%s.jpg' % (FOLDER_SAVE, hero_name, cover_name)  # 生成图片文件名
        if os.path.exists(file_path):  # 避免重复下载
            print('[exists]')
            continue
        # 样例：http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/152/152-bigskin-2.jpg
        url_img = URL_HERO_COVER_IMG % (hero_id, hero_id, i + 1)  # 生成海报图片URL
        request.urlretrieve(url_img, file_path)
        print('[ok]')


def download_all():
    print('start to download')
    res = request.urlopen(URL_HERO)
    data = res.read().decode('utf-8')
    data_json = json.loads(data)
    for hero_data in data_json:
        # 样例：{'ename': 105, 'cname': '廉颇', 'title': '正义爆轰', 'new_type': 0, 'hero_type': 3, 'skin_name': '正义爆轰|地狱岩魂'}
        download_cover(int(hero_data['ename']),
                       hero_data['cname'],
                       hero_data['skin_name'].split('|'))
    print('all done')


if __name__ == '__main__':
    download_all()
  
