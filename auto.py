import time
import random
import datetime
import pyautogui
from obswebsocket import obsws, requests
import random
def hide_current_scene_item(obs_host, obs_port, obs_password):
    ws = obsws(obs_host, obs_port, obs_password)
    ws.connect()
    for q in range(1,10):
        a=str(q)
        abs=ws.call(requests.GetSourceActive(sourceName=a)).datain
        if abs["videoActive"]==True:
            sources = ws.call(requests.GetSceneItemId(sceneName='场景',sourceName=a)).datain
            ws.call(requests.SetSceneItemEnabled(sceneName='场景',sceneItemId=sources['sceneItemId'],sceneItemEnabled=False))
            x=random.randint(1,9)
            xx=str(x)
            sources2 = ws.call(requests.GetSceneItemId(sceneName='场景',sourceName=xx)).datain
            ws.call(requests.SetSceneItemEnabled(sceneName='场景',sceneItemId=sources2['sceneItemId'],sceneItemEnabled=True))
            break
        if(q>=9):
            x=random.randint(1,9)
            xx=str(x)
            sour = ws.call(requests.GetSceneItemId(sceneName='场景',sourceName=xx)).datain
            ws.call(requests.SetSceneItemEnabled(sceneName='场景',sceneItemId=sour['sceneItemId'],sceneItemEnabled=True))
            break
        # 断开连接
    ws.disconnect()


def auto_answer_dingtalk_meeting():
    while True:
        # 获取指定位置的颜色
        color_at_location = pyautogui.pixel(2450,1413)
        # 判断颜色是否为 (0, 184, 83)
        if color_at_location == (0, 184, 83):
            time.sleep(10)
            # 如果颜色匹配，点击该位置
            pyautogui.click(x=2450, y=1413)
            #隐藏当前obs的视频
            hide_current_scene_item("ip","port","password")
            #等待之后开启摄像头
            time.sleep(12)
            pyautogui.moveTo(x=736, y=1189,duration=2)
            time.sleep(1)
            pyautogui.click(x=736, y=1189)
            color_at_location2 = pyautogui.pixel(627,1181)
            if color_at_location2 ==(210, 210, 211):
                pyautogui.moveTo(x=627, y=1181,duration=1)
                pyautogui.click(x=627, y=1181)
        time.sleep(5)  # 每隔5秒轮询一次

if __name__ == "__main__":
    auto_answer_dingtalk_meeting()