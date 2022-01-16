#import pandas as pd
#import numpy as np
import streamlit as st
import io
import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

KEY = "3093cf2f7b3a4ebba43b0d76a5501527"
ENDPOINT = "https://20220116sakurai.cognitiveservices.azure.com/"

headers = {
        "Content-Type": "application/octet-stream",
        "Ocp-Apim-Subscription-Key": KEY
    }
params = {
    "returnFaceId": "true",
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
}
GENDER_JP = {
    "female": "女",
    "male" : "男"
}

assert KEY

face_api_url = ENDPOINT + 'face/v1.0/detect'

st.title("顔認識アプリ")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    with io.BytesIO() as output:
        img.save(output, format="JPEG")
        binary_img = output.getvalue() #バイナリ取得
    res = requests.post(face_api_url, params=params, headers=headers, data=binary_img)
    results = res.json()
    draw = ImageDraw.Draw(img)

    for result in results:
        rect = result['faceRectangle']
        font = ImageFont.truetype("GenShinGothic-Bold.ttf", int(float(rect["width"])*0.17))
        text = GENDER_JP[result['faceAttributes']["gender"]]+ ":" + str(result['faceAttributes']["age"])
        draw.rectangle([(rect["left"], rect["top"]),(rect["left"]+rect["width"], rect["top"]+rect["height"])], fill=None, outline="green", width=3)
        draw.rectangle([(rect["left"], rect["top"]-float(rect["height"])*0.3),(rect["left"]+rect["width"], rect["top"])] , fill = "green", outline="green")
        draw.text((rect["left"]+5, rect["top"]-float(rect["height"])*0.3), text ,(225,225,225),font=font)

    st.image(img, caption="Uploaded Image.", use_column_width=True)

