from flask import Flask, request
from gevent.wsgi import WSGIServer
app = Flask(__name__)
from flask import render_template


def get_sections():
    ret = []
    ret.append({'src': '//ws-na.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=US&source=ac&ref=tf_til&ad_type=product_link&tracking_id=rubiq-20&marketplace=amazon&region=US&placement=B0009KF4GG&asins=B0009KF4GG&linkId=cfa928c627736841b950b24ab4b6e807&show_border=false&link_opens_in_new_window=false&price_color=333333&title_color=0066c0&bg_color=ffffff'})

@app.route('/store')
def store():
    return render_template('index.html', sections=get_sections())

@app.route('/')
def hello_world():
    return open('test.html').read()

if __name__ == '__main__':
    http_server = WSGIServer(('', 80), app)
    http_server.serve_forever()

