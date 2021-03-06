# -*- coding: utf-8 -*-
# !/usr/bin/python

<<<<<<< Updated upstream
# 第一步,提取特征
=======
# 绗竴姝�,鎻愬彇鐗瑰緛
>>>>>>> Stashed changes
def extract_feature(file_path):
    # 鎻愬彇涓�涓枃浠剁殑鐗瑰緛,杩斿洖鍊间负 鐗瑰緛鍚嶅瓧鍒楄〃 鍜� 鏁板�煎垪琛�
    return ['size', 'objects'], [10, 8]


all_file_paths = []  # 闇�瑕佹彁鍙栫壒寰佺殑鎵�鏈夋枃浠剁殑璺緞
for file_path in all_file_paths:
    feature_names, feature_nums = extract_feature(file_path)

    # 灏嗘墍鏈夌殑鐗瑰緛杞崲涓� "size_10" 杩欎釜褰㈠紡
    features = []
    for i in len(feature_names):
        feature = feature_names + '_' + str(feature_nums)
        features.append(feature)

    # 鏍囪鏄伓鎰忚繕鏄壇鎬�
    features.append('mal_or_ben_' + str(1))

    # 灏嗙壒寰佷繚瀛樺埌鏂囦欢
    # save(feature_path,features)

# 绗簩姝�,璇诲彇绗竴姝ヤ繚瀛樼殑鐗瑰緛
features_set = set()  # 鎵�鏈夌壒寰�
all_fea_paths = []
all_file_features = []
for fea_path in all_fea_paths:
    features = []

    # 鎵撳紑鐗瑰緛鏂囦欢,璇诲彇姣忎竴琛�
    f = open(fea_path)
    for line in f.readlines():
        str = line.split('_')
        feature_name = str[0]
        feature_num = int(str[1])

        # 鏇存柊鐗瑰緛闆嗗悎
        features_set.update(feature_names)

        # 淇濆瓨鐗瑰緛
        features.append({'name': feature_name, 'num': feature_num})
    all_file_features.append(features)

# 绗笁姝�,杞崲涓虹壒寰侀泦

# 鐢熸垚鐗瑰緛鎵�灞炵殑涓嬫爣
fea_index_dict = {}
for feature in features_set:
    fea_index_dict[feature] = len(fea_index_dict)

full_fea_list = []
for features in all_file_features:
    # 鍒濆鍖栨墍浠ョ壒寰佷负0
    fea_list = [0 for i in range(0, len(fea_index_dict))]
    for feature in features:
        fea_list[fea_index_dict[feature['name']]] = feature['num']

    # 淇濆瓨
    full_fea_list.append(fea_list)

# full_fea_list 灏辨槸浜岀淮琛ㄤ簡,鍏ㄦ槸鏁板瓧,杞崲涓�涓嬪氨鍙互浣跨敤鍒� 鏈哄櫒瀛︿範涓�
# 涓嬮潰浣跨敤pandas杩涜淇濆瓨
import pandas as pd

column_list = features_set
df = pd.DataFrame(full_fea_list, columns=column_list)

# 灏嗘暟鎹繚瀛�
df.to_csv('transfered.csv', index=False)

'''
# 涓嬫璇诲彇
def get_features(self):
    self.__df = pd.read_csv('transfered.csv')

    y_data = self.__df['mal_or_ben']
    del self.__df['mal_or_ben']

    X_data = np.array(self.__df)

    print('get_features() finished')
    return X_data, y_data
'''


