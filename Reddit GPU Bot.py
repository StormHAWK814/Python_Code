import requests
import time
import winsound
import datetime
import webbrowser

links = {"bb_FE":"https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440","bb_Gigabyte":"https://www.bestbuy.com/site/pny-geforce-rtx-3080-10gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432655.p?skuId=6432655"
         ,"bb_MSI":"https://www.bestbuy.com/site/msi-geforce-rtx-3080-ventus-3x-10g-oc-bv-gddr6x-pci-express-4-0-graphic-card-black-silver/6430175.p?skuId=6430175","bb_EVGA":"https://www.bestbuy.com/site/evga-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card/6432399.p?skuId=6432399"
         ,"bb_ASUS":"https://www.bestbuy.com/site/asus-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-strix-graphics-card-black/6432445.p?skuId=6432445#tabbed-customerreviews","bb_Gigabyte2":"https://www.bestbuy.com/site/gigabyte-geforce-rtx-3080-10g-gddr6x-pci-express-4-0-graphics-card-black/6430620.p?skuId=6430620"
         ,"bb_EVGA2":"https://www.bestbuy.com/site/evga-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card/6432400.p?skuId=6432400"}
headers = {"User-Agent":"Mozilla/5.0","cache-control":"max-age=0"}
is_sold_out_bb_FE = False
is_sold_out_bb_Gigabyte = False
is_sold_out_bb_MSI = False
is_sold_out_bb_EVGA = False
is_sold_out_bb_ASUS = False
is_sold_out_bb_Gigabyte2 = True
is_sold_out_bb_EVGA2 = False

def check():
    global is_sold_out_bb_FE
    global is_sold_out_bb_Gigabyte
    global is_sold_out_bb_MSI
    global is_sold_out_bb_EVGA
    global is_sold_out_bb_ASUS
    global is_sold_out_bb_Gigabyte2
    global is_sold_out_bb_EVGA2
    is_sold_out_bb_FE = check_single("bb_FE")
    is_sold_out_bb_Gigabyte = check_single("bb_Gigabyte")
    is_sold_out_bb_MSI = check_single("bb_MSI")
    is_sold_out_bb_EVGA = check_single("bb_EVGA")
    is_sold_out_bb_ASUS = check_single("bb_ASUS")
    #is_sold_out_bb_Gigabyte2 = check_single("bb_Gigabyte2")
    is_sold_out_bb_EVGA2 = check_single("bb_EVGA2")

    print (datetime.datetime.now(),"\nIn stock: \n Best Buy: \n  FE: ",not is_sold_out_bb_FE,"\n  PNY: ",not is_sold_out_bb_Gigabyte,"\n  MSI: ",not is_sold_out_bb_MSI,"\n  EVGA: ",not is_sold_out_bb_EVGA,"\n  ASUS: ",not is_sold_out_bb_ASUS,"\n  Gigabyte 2: ",not is_sold_out_bb_Gigabyte2,"\n  EVGA 2: ",not is_sold_out_bb_EVGA2)
    if not is_sold_out_bb_FE or not is_sold_out_bb_Gigabyte or not is_sold_out_bb_MSI or not is_sold_out_bb_EVGA or not is_sold_out_bb_ASUS or not is_sold_out_bb_Gigabyte2 or not is_sold_out_bb_EVGA2:
        signal()


def check_single(link_url):
    source = requests.get(links[link_url], headers=headers).text
    is_sold_out = source.__contains__("class=\"btn btn-disabled btn-lg btn-block add-to-cart-button\"") or source.__contains__("Coming Soon</button></div></div>")
    if not is_sold_out:
        webbrowser.open(links[link_url])
        save_file = open(link_url+".html","w")
        save_file.write(source)
        save_file.close()
    time.sleep(0.2)
    return is_sold_out


def signal():
    while True:
        for i in range(1, 10):
            winsound.Beep(i * 100, 200)
        time.sleep(0.5)

while True:
    check()
    time.sleep(0.5)


