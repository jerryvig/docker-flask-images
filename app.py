from flask import Flask
from flask import render_template
import random
import sys

app = Flask(__name__)
py_version = sys.version

images = [
    'https://scontent-dfw5-1.cdninstagram.com/vp/11ce65125202a2563e37ca80c4073ec4/5D29552E/t51.2885-15/sh0.08/e35/p750x750/54513498_148307729539880_609293141912830587_n.jpg?_nc_ht=scontent-dfw5-1.cdninstagram.com',
    'https://scontent-dfw5-1.cdninstagram.com/vp/6b356d3f136a8faa54bb34cc05046629/5D33C52B/t51.2885-15/e35/37387565_815268915349314_1813443494266535936_n.jpg?_nc_ht=scontent-dfw5-1.cdninstagram.com',
    'https://scontent-dfw5-1.cdninstagram.com/vp/58d1dbd7004a8a4f996f4121a25f218c/5D42F312/t51.2885-15/sh0.08/e35/p750x750/51117053_168443184137500_4906785752208500825_n.jpg?_nc_ht=scontent-dfw5-1.cdninstagram.com',
    'https://scontent-dfw5-1.cdninstagram.com/vp/ca7dd28803fa6b9fa77064ef80457715/5D446FE2/t51.2885-15/e35/18811957_449858388698118_541074327773118464_n.jpg?_nc_ht=scontent-dfw5-1.cdninstagram.com',
    'https://scontent-dfw5-1.cdninstagram.com/vp/b7e7fd3bc77c6da6b39c695deed1ec84/5D2B5B34/t51.2885-15/e35/52794914_574288159724489_7606902959612661009_n.jpg?_nc_ht=scontent-dfw5-1.cdninstagram.com',
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url, py_version=py_version)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

