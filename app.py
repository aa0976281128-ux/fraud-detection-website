from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# 1. 金融詐騙常見關鍵字資料庫 (Keyword Matching)
keywords = ['帳戶異常', '立即盜證', '轉帳', 'OTP', '登入', '連結', '投資', '退款']

# 2. 模擬歷史資料 (用於訓練隨機森林)
data = {
    'amount': [500, 80000, 200, 95000, 1200, 50000],
    'is_midnight': [0, 1, 0, 1, 0, 1],        # 1代表半夜交易
    'is_frequent': [0, 1, 0, 1, 0, 1],        # 1代表短時間多次轉帳
    'text_score': [0, 4, 0, 5, 0, 3],         # 文字風險分數
    'is_fraud': [0, 1, 0, 1, 0, 1]            # 1代表詐騙
}
df = pd.DataFrame(data)

# 3. 初始化隨機森林模型並完成訓練
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(df[['amount', 'is_midnight', 'is_frequent', 'text_score']], df['is_fraud'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/check', methods=['POST'])
def check_fraud():
    try:
        data = request.json
        user_message = data.get('message', '')
        amount = data.get('amount', 0)
        is_midnight = data.get('is_midnight', 0)
        is_frequent = data.get('is_frequent', 0)
        
        # 5. 執行關鍵字比對 (Rule-based System)
        matched_words = [w for w in keywords if w in user_message]
        text_score = len(matched_words)
        
        # 6. 模擬同時發生的交易行為特徵 (帶入機器學習大腦計算機率)
        prob = model.predict_proba([[amount, is_midnight, is_frequent, text_score]])[0][1]
        
        # 7. 輸出結果與即時警訊 (Expected Features)
        result = {
            'matched_words': matched_words if matched_words else '無',
            'text_score': text_score,
            'fraud_probability': round(prob * 100, 1),
            'is_fraud': prob > 0.6 or text_score >= 2
        }
        
        if result['is_fraud']:
            result['status'] = '⚠️ 警訊：偵測到高風險內容！請立刻提高警覺、取消或暫停交易！'
            result['status_type'] = 'danger'
        else:
            result['status'] = '✅ 狀態：目前檢測安全，請繼續保持防詐意識。'
            result['status_type'] = 'success'
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
