from flask import Flask, jsonify, json, Response
import stock.stock_price as stock

app = Flask(__name__)


# 获取所有数据
@app.route('/stock', methods=['GET'])
def get_data():
    data = stock.query_stock_price("CNY", "053d824a2d4bef851371ba85")
    # 使用 json.dumps 进行手动编码
    json_result = json.dumps(data, ensure_ascii=False)

    # 返回响应
    return Response(json_result, content_type='application/json; charset=utf-8')


if __name__ == '__main__':
    app.run(debug=True)
