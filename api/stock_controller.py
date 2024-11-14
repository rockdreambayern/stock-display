from flask import json, Response, Blueprint, render_template
import stock.stock_price as stock

stock_controller = Blueprint('stock_controller', __name__)


# 获取所有数据
@stock_controller.route('/stock', methods=['GET'])
def get_data():
    data = stock.query_multiple_stock_price("CNY")
    # 使用 json.dumps 进行手动编码
    json_result = json.dumps(data, ensure_ascii=False)

    # 返回响应
    return Response(json_result, content_type='application/json; charset=utf-8')

@stock_controller.route('/stock_latest/<string:code>', methods=['GET'])
def get_lastest_data(code):
    data = stock.query_stock_history_prices(code)

    # 使用 json.dumps 进行手动编码
    json_result = json.dumps(data, ensure_ascii=False)

    # 返回响应
    return Response(json_result, content_type='application/json; charset=utf-8')


@stock_controller.route('/', methods=['GET'])
def index():
    return render_template('index.html')
