import requests
import time
import winsound
import datetime
import webbrowser

links = {"Amazon_Palit":"https://www.amazon.co.uk/Palit-3060-StormX-GDDR6-NE63060019K9-190AF/dp/B08WRC2ZTD/ref=sr_1_3?crid=2KBT5QKANM6S0&keywords=3060&qid=1636405516&sprefix=3060%2Caps%2C84&sr=8-3",
"Amazon_MSI" : "https://www.amazon.co.uk/MSI-GeForce-Graphics-DisplayPort-TriFrozr/dp/B096SN631Y/ref=sr_1_2?keywords=3060+ti&qid=1636449681&sr=8-2",
"Amazon_Gigabyte":"https://www.amazon.co.uk/Gigabyte-GeForce-GAMING-V3-Graphics/dp/B096XZZ92Q/ref=sr_1_4?keywords=3060+ti&qid=1636449759&sr=8-4",
"Amazon_ASUS": "https://www.amazon.co.uk/ASUS-DUAL-RTX3060TI-O8G-V2-RTX3060TI-HDMI-90YV0G1J-M0NA00/dp/B098R4K8PV/ref=sr_1_3?keywords=3060+ti&qid=1636449815&refinements=p_72%3A419153031%2Cp_76%3A419158031&rnid=419157031&rps=1&sr=8-3"}

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36","cache-control":"max-age=0"}

is_sold_out_Amazon_Palit = False
is_sold_out_Amazon_MSI = False
is_sold_out_Amazon_Gigabyte = False
is_sold_out_Amazon_ASUS = False

def check():
    global is_sold_out_Amazon_