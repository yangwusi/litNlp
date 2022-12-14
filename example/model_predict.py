# -*- coding: utf-8 -*-
# @Time: 2020/6/21 0021 14:07
from litNlp.predict import SA_Model_Predict
import numpy as np
# 初始化模型
tokenize_path = 'model/tokenizer.pickle'
sa_model_path_m = 'model/model.h5'
# e_comment
predict_text = ['这个我不喜欢', '这个我喜欢不']
model = SA_Model_Predict(tokenize_path, sa_model_path_m, max_len=100)
sa_score = model.predict(predict_text)
# 情感极性概率
print([i[1] for i in sa_score])
# 情感label输出
print([np.argmax(i) for i in sa_score])