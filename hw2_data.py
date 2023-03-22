import streamlit as st
from io import StringIO
import pandas as pd

st.title('Word Frequency Calculator by 王彥成')
word_count = {}

filename = st.file_uploader('Upload your txt file', type='txt')
if filename is not None: #搭配streamlit執行之行為，避免使用者尚未上傳檔案就執行後面的程式
    string = StringIO(filename.getvalue().decode("utf-8")).read() #讀取檔案，並將byte值轉成字串
    word_list = string.split()
    for word in word_list:
        #計算出現次數，如果字典中沒有這個字，則新增並將出現次數設為1
        word_count[word] = word_count.get(word, 0)+1
    
    #讓字典依照出現次數由大到小排列
    sorted_list = dict(sorted(word_count.items(), key=lambda item: item[1], reverse = True))
    #分析資訊
    st.write("總共有", len(word_count), "個不重複的字")
    st.write("每一個英文字出現次數為：",sorted_list)
    #製作長條圖
    st.bar_chart(pd.DataFrame.from_dict(sorted_list, columns = ["word count"], orient = "index"))
