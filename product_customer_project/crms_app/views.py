from re import I
from django.shortcuts import render, redirect
from crms_app.models import *
from crms_app.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
login_URL = "/crms/testLogin/"

def customerHome(request):
    return render(request, 'crms_app/pages/home.html')

def catalogCustomer(request):
    return render(request, 'crms_app/pages/catalogCustomer.html')

def catalogMonthly(request):
    return render(request, 'crms_app/pages/catalogMonthly.html')

def catalogProduct(request):
    products = Product.objects.filter(isarchived=False)
    products = [
        {
            "category": "speakers",
            "name": "COD Super Bass JBL Charge 3+ Mini Portable Bluetooth Speaker",
            "ratings": [1, 2, 1, 10, 45],
            "stocks": 100,
            "reorderlvl": 20,
            "sellingprice": 179,
            "discount": 24,
            "isarchived": False
        },
        {
            "category": "speakers",
            "name": "120 Mini Portable Wireless Bluetooth Karaoke Speaker with FREE MICROPHONE",
            "ratings": [8, 2, 15, 60, 110],
            "stocks": 80,
            "reorderlvl": 20,
            "sellingprice": 899,
            "discount": 79,
            "isarchived": False
        },
        {
            "category": "speakers",
            "name": "JBL Charge MINI2+ plus Portable Wireless Bluetooth Speaker High Quality",
            "ratings": [3, 1, 9, 15, 60],
            "stocks": 69,
            "reorderlvl": 20,
            "sellingprice": 399,
            "discount": 58,
            "isarchived": False
        },
        {
            "category": "speakers",
            "name": "Original Super Bass Portable Bluetooth Speaker with Mic BT-1308 BT-1315 (3 inch) Wireless Bluetooth",
            "ratings": [12, 2, 6, 15, 92],
            "stocks": 21,
            "reorderlvl": 20,
            "sellingprice": 100,
            "discount": 75,
            "isarchived": False
        },
        {
            "category": "speakers",
            "name": "S6U/s10u Portable Mini LED Bluetooth Speaker",
            "ratings": [4, 0, 5, 8, 42],
            "stocks": 120,
            "reorderlvl": 20,
            "sellingprice": 75,
            "discount": 22,
            "isarchived": False
        },
        {
          "category": "speakers",
          "name": "118 Mini Portable Wireless Bluetooth Karaoke Speaker with FREE MICROPHONE",
          "ratings": [5,14,4,2,134],
          "stocks": 1080,
          "reorderlvl": 110,
          "sellingprice": 900,
          "discount": 81,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "V2S Speaker VS802 Bluetooth Speaker With FM Radio Portable Rechargable TF Card USB MP3 Mini Wireless Player Free VS55 Foldable Mini USB LED Light",
          "ratings": [13,22,19,17,1],
          "stocks": 3398,
          "reorderlvl": 200,
          "sellingprice": 558,
          "discount": 52,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "Zeus Z-350 2.1 25Watts/Peak 60Watts Bluetooth Speakers Noise reduction Desk Speakers W/ Subwoofer CD A350",
          "ratings": [9,24,22,7,54],
          "stocks": 4920,
          "reorderlvl": 240,
          "sellingprice": 1999,
          "discount": 64,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "Wireless Bluetooth Speakers led light Karaoke Portable Super Bass LED with Free Microphone",
          "ratings": [8,7,43,85,17],
          "stocks": 915,
          "reorderlvl": 230,
          "sellingprice": 599,
          "discount": 73,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "120 Wireless Bluetooth Speaker with FREE MICROPHONE",
          "ratings": [24,3,32,1,187],
          "stocks": 5331,
          "reorderlvl": 20,
          "sellingprice": 870,
          "discount": 80,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "Ama good shop KUKU 5 inch Bluetooth Speaker USB TF AUX player",
          "ratings": [4,17,25,47,164],
          "stocks": 3984,
          "reorderlvl": 120,
          "sellingprice": 799,
          "discount": 39,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "Suntex Apollo Supreme PRO Original Wireless 5.0 Bluetooth Speaker For Sale Audio Sound Bar Original FM AUX With Mic Answer Phone Compatible Phone Tablet With SD Card Slot Wireless PC Desktop Sound Bar TV Speaker",
          "ratings": [11,1,50,99,54],
          "stocks": 3184,
          "reorderlvl": 60,
          "sellingprice": 1299,
          "discount": 58,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "8Inch Karaoke Wireless Bluetooth Portable  Speaker with FREE wire MIC",
          "ratings": [23,18,4,93,41],
          "stocks": 4279,
          "reorderlvl": 150,
          "sellingprice": 1500,
          "discount": 62,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "COD JBL Charge 3 Mini Portable Bluetooth Speaker Charge 3+ MINI Super Bass wireless Speaker Music Stereo Outdoor Music",
          "ratings": [6,6,8,34,114],
          "stocks": 2278,
          "reorderlvl": 20,
          "sellingprice": 378,
          "discount": 54,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "EZEEY S4 Portable USB 3.5mm Multimedia Speaker for Desktop Laptop Notebook Tablet SmartPhones PC Speaker",
          "ratings": [0,6,16,65,188],
          "stocks": 4197,
          "reorderlvl": 120,
          "sellingprice": 3180,
          "discount": 95,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "KaraokeStereo Portable Wireless  with DISCO Light and Strap Bluetooth Speaker with FREE Wired Microphone SK-1101",
          "ratings": [14,1,14,42,189],
          "stocks": 4879,
          "reorderlvl": 80,
          "sellingprice": 275,
          "discount": 87,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "Suntex Apollo Supreme Max Original Bluetooth 5.0 Wireless Speaker Sale Audio Soundbar Speaker Original FM AUX with Mic to answer calls compatible for mobile phones Computer Tablet with SD card Slot Wireless Speaker for pc desktop computer TV Speakers",
          "ratings": [14,22,2,68,112],
          "stocks": 1967,
          "reorderlvl": 220,
          "sellingprice": 2999,
          "discount": 69,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "Ama Good Shop NEW KIMISO QS-222 2X8 inches Portable Bluetooth Wireless Speaker Karaoke with Remote and Mic",
          "ratings": [12,2,45,5,161],
          "stocks": 4127,
          "reorderlvl": 80,
          "sellingprice": 1999,
          "discount": 46,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "JBL GO 3 Portable Wireless Bluetooth Speaker go3 jbl Waterproof speaker",
          "ratings": [5,23,10,1,181],
          "stocks": 4171,
          "reorderlvl": 90,
          "sellingprice": 3299,
          "discount": 70,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "KTS-1091 KARAOKE  Super Bass Portable Wireless Bluetooth Speaker KTS-1091 With Free Mic",
          "ratings": [10,16,9,58,125],
          "stocks": 3507,
          "reorderlvl": 110,
          "sellingprice": 1999,
          "discount": 69,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "SK-ONE Karaoke Stereo Portable Wireless with DISCO Light and Strap Bluetooth Speaker with FREE Wired Microphone SK-1101",
          "ratings": [23,5,9,7,234],
          "stocks": 5390,
          "reorderlvl": 200,
          "sellingprice": 500,
          "discount": 38,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "TG113 T113 Bluetooth Speaker Wireless Super Bass Outdoor Splashproof Wireless Bluetooth Speaker Portable waterproof speaker FM/TF/USB 3D",
          "ratings": [0,18,2,26,157],
          "stocks": 1295,
          "reorderlvl": 180,
          "sellingprice": 358,
          "discount": 54,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "【SIIIM9】Portable Wireless Bluetooth Speaker With Mic Stereo Dual KTS-1062 Rechargeable Portable Karaoke Wireless Speaker With Free Mic KTS 1062 Wired Microphone Support USB TF FM AUX Function",
          "ratings": [21,23,21,27,104],
          "stocks": 3257,
          "reorderlvl": 60,
          "sellingprice": 8999,
          "discount": 97,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "✅100% Original Jcam OP-330 Karaoke LED Flashing lights  Portable Wireless Bluetooth Speaker TWS/FM/USB/TF Function",
          "ratings": [11,2,12,11,47],
          "stocks": 5988,
          "reorderlvl": 50,
          "sellingprice": 3598,
          "discount": 99,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "Super Bass 8 Inch Karaoke Wireless Bluetooth Speaker with FREE MICROPHONE 1090D",
          "ratings": [19,17,22,7,115],
          "stocks": 1361,
          "reorderlvl": 150,
          "sellingprice": 800,
          "discount": 31,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "119 Mini Portable Wireless Bluetooth Karaoke Speaker with FREE MICROPHONE",
          "ratings": [8,15,43,69,284],
          "stocks": 1439,
          "reorderlvl": 90,
          "sellingprice": 870,
          "discount": 80,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "TBL Charge 2+ Charge mini portable Bluetooth Speaker Wireless Splash proof  Waterproof Stereo Music",
          "ratings": [16,11,28,53,45],
          "stocks": 3114,
          "reorderlvl": 220,
          "sellingprice": 340,
          "discount": 52,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "5inch Karaoke Portable Wireless Speaker with stand With FREE Mic 1090Bmini",
          "ratings": [1,20,43,46,1],
          "stocks": 2138,
          "reorderlvl": 250,
          "sellingprice": 600,
          "discount": 61,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "【SIIIM9】Original JBL Charge 3+ Mini Portable Bluetooth Wireless Speaker Multicolor Luminous Portable Bluetooth Wireless Speaker Splashproof With Built-in Powerbank JBL Charge 3+ Speaker-",
          "ratings": [9,7,10,33,71],
          "stocks": 1793,
          "reorderlvl": 150,
          "sellingprice": 800,
          "discount": 75,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "JBL XTREME Big Bluetooth Splashproof Portable Wireless Speaker Extreme Waterproof speaker",
          "ratings": [2,19,28,47,224],
          "stocks": 1366,
          "reorderlvl": 180,
          "sellingprice": 878,
          "discount": 56,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "JBL Charge 2  Portable Bluetooth Wireless Speaker Splashproof with Builtin Powerbank Speaker speaker wireless audio Audio Bluetooth Speaker﹍",
          "ratings": [3,12,26,54,220],
          "stocks": 1169,
          "reorderlvl": 110,
          "sellingprice": 850,
          "discount": 35,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "Awei Y669 Bluetooth Outdoor TWS Waterproof Portable Wireless Speaker",
          "ratings": [19,10,25,38,100],
          "stocks": 4002,
          "reorderlvl": 130,
          "sellingprice": 2099,
          "discount": 32,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "【Buy 1 Get 1】Portable  Mini LED Bluetooth Speaker Wireless Outdoor Music Surround Stereo Charge  Bass  Loudspeaker",
          "ratings": [8,2,41,75,156],
          "stocks": 1465,
          "reorderlvl": 200,
          "sellingprice": 299,
          "discount": 22,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "JBL Charge 2+ Big Portable Wireless Bluetooth Speaker With Built-in Powerbank",
          "ratings": [17,10,42,5,166],
          "stocks": 4012,
          "reorderlvl": 220,
          "sellingprice": 850,
          "discount": 35,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "New Portable Wireless Bluetooth Speaker With Mic Stereo Dual KTS-1062 Rechargeable Portable Karaoke Wireless Speaker With Free Mic KTS 1062 Wired Microphone Support USB TF FM AUX Function",
          "ratings": [21,25,20,74,165],
          "stocks": 2561,
          "reorderlvl": 140,
          "sellingprice": 899,
          "discount": 69,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "Flagship Portable LED Bluetooth Mini Speaker Support phone/Laptop/Tablet PC/TF card/Mini micro card Wireless Bluetooth Speaker Portable Line-In Speakers",
          "ratings": [9,20,36,44,129],
          "stocks": 2983,
          "reorderlvl": 50,
          "sellingprice": 370,
          "discount": 81,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "YUTU HF-S286 portable speaker bluetooth FM/TF/USB/AUX/led Flashing lights s286",
          "ratings": [16,19,46,88,281],
          "stocks": 1763,
          "reorderlvl": 160,
          "sellingprice": 350,
          "discount": 62,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "GREAT JBL Charge Mini 2+ Portable Wireless Bluetooth Speaker",
          "ratings": [15,21,33,91,211],
          "stocks": 3652,
          "reorderlvl": 60,
          "sellingprice": 850,
          "discount": 35,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "Ninja Gaming A-350 2.1 25Watts/Peak 60Watts Bluetooth Noise reduction Desk Speakers W/ Subwoofer",
          "ratings": [22,25,2,54,296],
          "stocks": 3339,
          "reorderlvl": 110,
          "sellingprice": 1999,
          "discount": 60,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "ITOP LED Space Eye Speaker RGC lights Dynamic Listening for Laptop PC TV Mobiel",
          "ratings": [12,19,38,48,29],
          "stocks": 5303,
          "reorderlvl": 50,
          "sellingprice": 599,
          "discount": 61,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "Computer Speaker T-WOLF S3 Usb 2.0 Desktop Speaker Dual speaker USB Wired Speaker",
          "ratings": [24,23,46,98,294],
          "stocks": 3718,
          "reorderlvl": 220,
          "sellingprice": 699,
          "discount": 70,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "super max store/KTS-1171 Portable Karaoke KTS-1171 wireless speaker kts 1171 bluetooth speaker kts1171",
          "ratings": [16,1,41,2,283],
          "stocks": 2871,
          "reorderlvl": 230,
          "sellingprice": 555,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "TG528  Best selling speaker with  radio Wireless Portable Bluetooth Proof Noise reduction Outdoor hands-free portable wireless bluetooth mini speaker with TF card, FM radio, USB function, smart touch speaker fashion super bass",
          "ratings": [23,23,29,27,290],
          "stocks": 792,
          "reorderlvl": 230,
          "sellingprice": 688,
          "discount": 57,
          "isarchived": 0
        },
        {
          "category": "speakers",
          "name": "Crown PA-1220 12\" 200W Instrumental Speaker (Black)",
          "ratings": [17,16,3,39,221],
          "stocks": 3015,
          "reorderlvl": 200,
          "sellingprice": 1099,
          "discount": 19,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "xMOWI RX3 Dual Mic Gaming Earphone - Red",
          "ratings": [7,25,9,71,241],
          "stocks": 1091,
          "reorderlvl": 200,
          "sellingprice": 450,
          "discount": 40,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "MKEPS Cat Ear Cute Wireless Bluetooth Headphones Gaming Noise Cancelling Headphone Sports Headset With Mic Usb Adjustable Foldable Volume Control Stereo HIFI Music LED Breathing Lamp Over-The-Ear Headphones For Phone IPad IPhone Pc Laptop Tablet P47/B39",
          "ratings": [5,17,45,90,202],
          "stocks": 754,
          "reorderlvl": 190,
          "sellingprice": 597,
          "discount": 70,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "S0ny Headphone 102dB Extra Bass Over-the-Ear Headphones Headset Stereo",
          "ratings": [10,22,8,96,145],
          "stocks": 1551,
          "reorderlvl": 20,
          "sellingprice": 500,
          "discount": 80,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "【OSO】P47 Wireless Bluetooth Headphones TF Card Stereo Radio Mp3 Player Foldable EDR Wireless Headset Also can put 3,5mm earphone wire connection",
          "ratings": [9,25,33,45,249],
          "stocks": 5088,
          "reorderlvl": 50,
          "sellingprice": 599,
          "discount": 76,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "【With free LED Watch】P47 Bluetooth Headphones TF Card/FM Stereo Radio Mp3 Player Foldable 4.2 EDR Wireless Headset",
          "ratings": [2,6,48,42,66],
          "stocks": 540,
          "reorderlvl": 170,
          "sellingprice": 499,
          "discount": 67,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "New WH-01 Wireless Bluetooth Headset with Bass Stereo and Card Slots, Supports Computers and Microphones",
          "ratings": [16,22,25,46,241],
          "stocks": 3031,
          "reorderlvl": 30,
          "sellingprice": 999,
          "discount": 61,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "NEW GAMING HEADPHONE HTM 996",
          "ratings": [22,5,17,25,172],
          "stocks": 5655,
          "reorderlvl": 10,
          "sellingprice": 320,
          "discount": 17,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "P47 Wireless Bluetooth On-Ear Headphone Headset",
          "ratings": [7,18,47,46,2],
          "stocks": 3797,
          "reorderlvl": 100,
          "sellingprice": 199,
          "discount": 25,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "CCL PH U24 High Quality Macaroon Earphones Candy Color In Ear Headset with Microphone",
          "ratings": [2,1,4,48,118],
          "stocks": 3851,
          "reorderlvl": 50,
          "sellingprice": 327,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "Original Razer Kraken Pro V2 Gaming Headset Gaming Headset With Light Gaming Headset For Girls Gaming Headset With Led Light Earphone Headphone Surround Sound Ultra-light Bendable Cardioid Microphone Ultra-light Ergonomic Build Gaming Headphones",
          "ratings": [19,5,16,54,60],
          "stocks": 2173,
          "reorderlvl": 200,
          "sellingprice": 19999.9,
          "discount": 90,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "for JBL t450bt Headphone Bluetooth Lipat Bass dengan Mic Noise Canceling",
          "ratings": [6,22,9,62,220],
          "stocks": 4427,
          "reorderlvl": 120,
          "sellingprice": 980,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "✅100% Original Meet  Headphone XB-450 Extra BassHeadset Stereo headphones",
          "ratings": [17,2,43,55,131],
          "stocks": 2975,
          "reorderlvl": 90,
          "sellingprice": 1598,
          "discount": 94,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "Original Earphone Universal In-Ear Headphones 3.5mm Headset Wired Control Earphones Authentic Plug with Mic Built-in Microphone Earbuds Headset Compatible for OPPO",
          "ratings": [21,4,25,91,221],
          "stocks": 5639,
          "reorderlvl": 140,
          "sellingprice": 599,
          "discount": 84,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "Audiobop Function Bass Wireless  EDR Bluetooth Headphones TF Card FM Radio Headphone BT602",
          "ratings": [11,7,13,42,164],
          "stocks": 5845,
          "reorderlvl": 190,
          "sellingprice": 500,
          "discount": 62,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "New Hellokitty Headset COD",
          "ratings": [7,20,49,90,150],
          "stocks": 2242,
          "reorderlvl": 190,
          "sellingprice": 400,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "Misde A3 Gaming Headset Stereo Headphone for Computer Headset",
          "ratings": [16,8,28,81,104],
          "stocks": 3146,
          "reorderlvl": 30,
          "sellingprice": 899,
          "discount": 75,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "Fast Delivery Original Razer Bluetooth Earphone TWS Wireless Headphones Touch Button Headset Stereo Sports Earbuds Charging Box LED Battery Indicator For iOS Android Xiaomi Huawei ipod",
          "ratings": [22,23,41,95,229],
          "stocks": 3808,
          "reorderlvl": 100,
          "sellingprice": 996,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "AIKAS AI-A3 Headset wired gaming headset with headset stereo 3.5mm microphone retractable headset gaming headset",
          "ratings": [1,13,17,88,26],
          "stocks": 2015,
          "reorderlvl": 160,
          "sellingprice": 500,
          "discount": 60,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "MGall Original Cat Ear Headphones Bluetooth Wireless Headsets built-in mic headphone girl's Gift gaming heads",
          "ratings": [3,8,27,78,128],
          "stocks": 5725,
          "reorderlvl": 10,
          "sellingprice": 1999,
          "discount": 90,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "Headphone Stand Aluminum Alloy Headset Stand Holder Headphone Display Holder Easy Installation Aluminum Gaming Headset Stand Display Holder Wholesale Stylish Simple Design Earphone Earphones Headphones Headset Holder Gaming Accessories Headphone Hanger",
          "ratings": [13,20,11,16,72],
          "stocks": 5892,
          "reorderlvl": 110,
          "sellingprice": 199,
          "discount": 41,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "V2S Headphone K4Pro 3.5mm Wired Headphones Gaming Headset Stereo Sound Headphone With Microphone",
          "ratings": [18,2,47,9,132],
          "stocks": 5421,
          "reorderlvl": 230,
          "sellingprice": 999,
          "discount": 56,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "UNIVERSAL WIRELESS BLUETOOTH HEADSET",
          "ratings": [17,0,12,76,37],
          "stocks": 5257,
          "reorderlvl": 230,
          "sellingprice": 388,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "l4UP47 Wireless Bluetooth On-Ear Headphone Headset Bluetooth Headphones COD",
          "ratings": [11,7,46,90,275],
          "stocks": 2421,
          "reorderlvl": 180,
          "sellingprice": 459,
          "discount": 30,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "EDIFIER W600BT Wireless Bluetooth Headphone Bluetooth 5.1 up to 30hrs Playback Time 40mm Drivers Hands-Free Headset",
          "ratings": [5,5,5,89,274],
          "stocks": 2569,
          "reorderlvl": 180,
          "sellingprice": 1699,
          "discount": 36,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "Samsung Original Earphone Universal In-Ear Headphones 3.5mm Headset Wired Control Earphones Authentic Plug with Mic Built-in Microphone Earbuds Headset",
          "ratings": [1,24,10,91,219],
          "stocks": 4301,
          "reorderlvl": 230,
          "sellingprice": 599,
          "discount": 84,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "TECNO Earphone Original Universal In-Ear Headphones 3.5mm Headset Wired Control Earphones Authentic Plug with Mic Built-in Microphone Earbuds Headset",
          "ratings": [1,16,4,46,294],
          "stocks": 2489,
          "reorderlvl": 140,
          "sellingprice": 599,
          "discount": 84,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "Miniso Foldable Headphone Music Tune ABS Comfortable Rotatable Adjustable Wired On Ear Headphones",
          "ratings": [23,2,14,42,139],
          "stocks": 1511,
          "reorderlvl": 120,
          "sellingprice": 499,
          "discount": 20,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "Realme Original Earphone Universal In-Ear Headphones 3.5mm Headset Wired Control Earphones Authentic Plug with Mic Built-in Microphone Earbuds Headset",
          "ratings": [4,17,1,43,63],
          "stocks": 3207,
          "reorderlvl": 140,
          "sellingprice": 599,
          "discount": 87,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "B39 Wireless Bluetooth 5.0 Headset with Mic Colorful Led Lights Gaming Over-ear Stereo Headphone Noise Cancellation Folding Compact Support TF Card 3.5mm Plug Built-in Fm Mp3 Player",
          "ratings": [12,8,30,93,198],
          "stocks": 3652,
          "reorderlvl": 50,
          "sellingprice": 311,
          "discount": 42,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "MKEPS LED Gaming Headphones USB&3.5MM AUX Wired Headsets With Microphone 7.1 Surround Sound Retractable Active Noise Cancelling Headphone Over Ear Earphone For Pc Laptop Computer Gaming Accessories",
          "ratings": [16,5,46,22,202],
          "stocks": 2834,
          "reorderlvl": 210,
          "sellingprice": 209,
          "discount": 77,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "【XMT】DT-326 wired earphone White elegant stereo hi-fi earphone with microphone, suitable for PC/Mobile phones/notebooks/tablets, etc computer telephone game noise reduction earphone",
          "ratings": [2,12,4,93,172],
          "stocks": 3672,
          "reorderlvl": 230,
          "sellingprice": 1288,
          "discount": 75,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "V2S SE5888 Collapsible 3.5mm Jack Wired Headphone Foldable Adjustable Headset game headphones",
          "ratings": [10,3,30,10,19],
          "stocks": 3108,
          "reorderlvl": 180,
          "sellingprice": 600,
          "discount": 67,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "New TWS Wireless Bluetooth Headphones HiFi Stereo Noise Canceling Gaming Headset With Mic Macaron Colors Sports Deep Bass ANC On-ear Earphones",
          "ratings": [19,9,16,60,171],
          "stocks": 4974,
          "reorderlvl": 180,
          "sellingprice": 1285,
          "discount": 69,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "Xiaomi Redmi Earphone Original Universal In-Ear Headphones 3.5mm Headset Wired Control Earphones Authentic Plug with Mic Built-in Microphone Earbuds Headset",
          "ratings": [2,5,36,17,13],
          "stocks": 3169,
          "reorderlvl": 80,
          "sellingprice": 599,
          "discount": 85,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "QMEOW Tiktok LED Gaming Headphone HiFi 4D Stereo Headset with Microphone For PC Laptop Games",
          "ratings": [2,18,13,18,166],
          "stocks": 2415,
          "reorderlvl": 0,
          "sellingprice": 700,
          "discount": 57,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "Razer BlackShark V2 X HyperClear Cardioid Mic Gaming Headphones TriForce 50mm Drivers",
          "ratings": [13,14,29,86,209],
          "stocks": 2596,
          "reorderlvl": 80,
          "sellingprice": 3999,
          "discount": 43,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "【BUY 1 TAKE BAG】Earphones with Mic  Surround Sound Bass HIFI Stereo Wired Earphone Original Headset Gaming Earphone Waterproof Sweat-proof Sport Earbuds HD Stereo Sport Running Handsfree for Samsung/Xiaomi/ Huawei/Oppo/Vivo COD",
          "ratings": [8,7,40,4,169],
          "stocks": 3450,
          "reorderlvl": 230,
          "sellingprice": 599,
          "discount": 86,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "J59S Wireless Bluetooth Super Bass Stereo On-Ear Headphone Headset",
          "ratings": [24,16,13,18,128],
          "stocks": 1726,
          "reorderlvl": 140,
          "sellingprice": 450,
          "discount": 24,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "P47 Wireless Bluetooth On-Ear Headphone Headset Bluetooth Headphones",
          "ratings": [1,2,7,31,69],
          "stocks": 3741,
          "reorderlvl": 50,
          "sellingprice": 599,
          "discount": 78,
          "isarchived": 0
        },
        {
          "category": "headsets",
          "name": "XO EP10 High Fidelity In Ear Earphone - Black",
          "ratings": [8,22,7,92,8],
          "stocks": 1510,
          "reorderlvl": 40,
          "sellingprice": 299,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "HUG Wired Microphone - H98-039",
          "ratings": [0,1,33,52,76],
          "stocks": 4014,
          "reorderlvl": 0,
          "sellingprice": 129,
          "discount": 62,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "HUG H98-600 Professional Dynamic Handheld Wired Microphone",
          "ratings": [19,8,4,83,53],
          "stocks": 1335,
          "reorderlvl": 140,
          "sellingprice": 356,
          "discount": 75,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "SN-630  Microphone Karaoke Microphone",
          "ratings": [14,6,19,78,24],
          "stocks": 3925,
          "reorderlvl": 110,
          "sellingprice": 200,
          "discount": 56,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "✅100% Original Smilee New Professional Y-699 Model Heavy Duty 10M Wire microphone",
          "ratings": [21,5,14,31,11],
          "stocks": 1223,
          "reorderlvl": 210,
          "sellingprice": 3598,
          "discount": 95,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "✅100% Original Smilee Heavy Duty Wired microphone for videoke SN-8.9",
          "ratings": [4,1,0,19,283],
          "stocks": 2320,
          "reorderlvl": 200,
          "sellingprice": 3598,
          "discount": 95,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Original Crown M-800 Dynamic Microphone Hyper Cardioid Dynamic Microphone Wired Microphone Bouncing Mic",
          "ratings": [7,18,17,59,171],
          "stocks": 1126,
          "reorderlvl": 170,
          "sellingprice": 850,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "[Local seller] USB Computer condenser recording microphone with desktop stand, suitable for Youtube podcasts, musical instruments, live...",
          "ratings": [5,20,30,31,154],
          "stocks": 336,
          "reorderlvl": 210,
          "sellingprice": 1299,
          "discount": 62,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "WS 858 Karaoke KTV MicBluetooth Wireless Handheld Microphone & HiFi Speaker for Mobile Phone Portable Karaoke",
          "ratings": [23,17,21,69,195],
          "stocks": 1198,
          "reorderlvl": 120,
          "sellingprice": 995,
          "discount": 84,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Fifine K669B K669 USB Microphone Metal Condenser Microphone Recording Microphone for MAC or Windows laptop PC microphone Cardioid Microphone Studio Recording Microphone Voice Overs Streaming microphone YouTube ASMR Vlog Gaming Podcast",
          "ratings": [2,15,13,72,67],
          "stocks": 4755,
          "reorderlvl": 70,
          "sellingprice": 5866,
          "discount": 80,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "With Free Foam New 100% Original Picture Platinum Heavy Duty Wired 10 Meter Microphone KS-5000 KS-3000 KS-8000",
          "ratings": [10,0,46,43,220],
          "stocks": 2518,
          "reorderlvl": 50,
          "sellingprice": 500,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Original BM800 USB Professional Condenser Microphone For Live Online Broadcasting Streaming Podcast",
          "ratings": [21,24,21,45,296],
          "stocks": 309,
          "reorderlvl": 150,
          "sellingprice": 1899,
          "discount": 70,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "✅100% Original Meet PL-1000 Heavy Duty Wired Microphone for Videok W/Hard Case",
          "ratings": [12,23,33,53,31],
          "stocks": 1037,
          "reorderlvl": 120,
          "sellingprice": 3598,
          "discount": 95,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "ICIC USB Microphone for Recording for Singing Condenser Microphone Full Set for MAC or Windows or Android Microphone for Videoke Complete Set Mic Condenser with Tripod Stand Desktop Bracket or Cantilever Bracket",
          "ratings": [6,21,41,35,279],
          "stocks": 4031,
          "reorderlvl": 90,
          "sellingprice": 4999,
          "discount": 90,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "The magic mirror store 100  Original Wireless Bluetooth Microphone WS-858 Karaoke Speaker",
          "ratings": [1,13,1,32,103],
          "stocks": 2886,
          "reorderlvl": 70,
          "sellingprice": 592,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Platinum Gold DM-6000s microphone/videoke/wire microphone",
          "ratings": [23,3,22,82,76],
          "stocks": 2943,
          "reorderlvl": 170,
          "sellingprice": 1100,
          "discount": 75,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "MINIMINISHOP Universal karaoke mic for kts serier kdx ktx etc, mic only",
          "ratings": [6,11,33,95,198],
          "stocks": 3421,
          "reorderlvl": 170,
          "sellingprice": 99,
          "discount": 61,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Carol Wired Microphone GS Series GS-55",
          "ratings": [16,16,23,55,89],
          "stocks": 5592,
          "reorderlvl": 50,
          "sellingprice": 2174,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "The magic mirror store New DM-520 Dynamic Handheld Wired Microphone with 6.35mm Plug Cable for Family Karaoke Singing Mic",
          "ratings": [24,25,39,39,195],
          "stocks": 737,
          "reorderlvl": 100,
          "sellingprice": 572,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Platinum Karaoke Professional Videoke Mirophone mic High-End Dynamic Wired mic  with heavy duty mic wire (original with 2D barcode/sticker )/tested before ship out",
          "ratings": [17,12,6,91,179],
          "stocks": 2708,
          "reorderlvl": 10,
          "sellingprice": 1599,
          "discount": 78,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Hyundai platinum DM8000 mic",
          "ratings": [16,15,3,99,212],
          "stocks": 3587,
          "reorderlvl": 40,
          "sellingprice": 499,
          "discount": 69,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "SHURE BLX-238S UHF Wireless Microphone For Videoke Dual Mic",
          "ratings": [5,7,10,31,68],
          "stocks": 3058,
          "reorderlvl": 30,
          "sellingprice": 2499,
          "discount": 62,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "ICIC USB Condenser Microphone for Recording Vlogging Videoke Studio Singing  Mic Condenser Complete Set MAC or Windows or Android Microphone Condenser Set with Tripod Stand Laptop",
          "ratings": [19,8,48,24,221],
          "stocks": 2573,
          "reorderlvl": 190,
          "sellingprice": 9999,
          "discount": 92,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Hyundai Platinum DM-8000 Professional Hyper-Cardioid Dynamic Gold Microphone",
          "ratings": [17,13,50,19,36],
          "stocks": 2182,
          "reorderlvl": 40,
          "sellingprice": 388,
          "discount": 57,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "HyperX QuadCast USB Condenser Full featured Standalone Gaming Microphone for streamers , content creators , and gamers , Discord , Red Led ( HX-MICQC-BK ) - Spoyl Store",
          "ratings": [7,21,23,52,3],
          "stocks": 3519,
          "reorderlvl": 40,
          "sellingprice": 6599,
          "discount": 45,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "The magic mirror store ✅100  Original Meet SN-630  Microphone Karaoke Microphone",
          "ratings": [23,20,20,90,190],
          "stocks": 5793,
          "reorderlvl": 40,
          "sellingprice": 531,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "SUNTECH ST-888s professional dynamic microphone with wireless",
          "ratings": [7,2,24,47,90],
          "stocks": 774,
          "reorderlvl": 240,
          "sellingprice": 1350,
          "discount": 80,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "U-J200 Dual Microphone Wireless Microphone for Professional Karaoke UHF",
          "ratings": [19,11,29,57,194],
          "stocks": 3776,
          "reorderlvl": 180,
          "sellingprice": 4416,
          "discount": 72,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Hyundai Platinum DM-8000 Microphone for Videoke/Karaoke Machine",
          "ratings": [17,5,2,69,289],
          "stocks": 4328,
          "reorderlvl": 250,
          "sellingprice": 350,
          "discount": 44,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Shure Sh-959/SM-90A microphone for videoke with good sound quality(tested before shipped out)",
          "ratings": [6,17,4,12,66],
          "stocks": 3510,
          "reorderlvl": 90,
          "sellingprice": 500,
          "discount": 43,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Sunask Microphone Original Microphone Wireless KTV Karaoke Bluetooth Handheld Mic",
          "ratings": [2,8,2,26,177],
          "stocks": 3511,
          "reorderlvl": 70,
          "sellingprice": 350,
          "discount": 46,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "MICROPHONE FOR VIDEOKE PLATINUM DM6000S KARAOKE WIRED MIC dm6000",
          "ratings": [1,15,48,60,278],
          "stocks": 2284,
          "reorderlvl": 140,
          "sellingprice": 150,
          "discount": 40,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Hyundai Platinum DM-8000 Dynamic Microphone",
          "ratings": [1,11,2,51,36],
          "stocks": 3017,
          "reorderlvl": 170,
          "sellingprice": 250,
          "discount": 34,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "100% oringinal yamaha heavy duty microphone YA-688 yamaha mic",
          "ratings": [19,18,43,38,184],
          "stocks": 2413,
          "reorderlvl": 130,
          "sellingprice": 999,
          "discount": 41,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Professional microphone system (tested before ship out)",
          "ratings": [25,15,34,97,90],
          "stocks": 1588,
          "reorderlvl": 10,
          "sellingprice": 399,
          "discount": 84,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Professional Condenser Microphone With V8 Sound Card Set Microphone Condenser For Live Online Broadcasting, Streaming, Podcast etc. (V8 Soundcard, Microphone, Pop Filter, NB35 Table Stand)",
          "ratings": [14,9,45,98,157],
          "stocks": 2540,
          "reorderlvl": 230,
          "sellingprice": 1999,
          "discount": 70,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "BlueWow J11 Wireless Lapel Microphone Lavalier Mic Noise Reduction Live Interview Mobile Phone Recording for iPhone Type C with Charging Box",
          "ratings": [16,11,48,92,65],
          "stocks": 746,
          "reorderlvl": 20,
          "sellingprice": 999,
          "discount": 4,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "✅100% Original Meet Pluspower 3.5mm Mini Studio Speech Microphone Clip On Lapel For PC",
          "ratings": [12,18,19,50,34],
          "stocks": 5616,
          "reorderlvl": 140,
          "sellingprice": 3598,
          "discount": 99,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Platinum DMD-5500 Wired Microphone 10 meter wire-good quality",
          "ratings": [21,19,7,45,132],
          "stocks": 685,
          "reorderlvl": 160,
          "sellingprice": 250,
          "discount": 36,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Platinum Karaoke Microphone for Videoke DM 6000s",
          "ratings": [7,6,30,85,200],
          "stocks": 1512,
          "reorderlvl": 40,
          "sellingprice": 488,
          "discount": 74,
          "isarchived": 0
        },
        {
          "category": "microphones",
          "name": "Professional Wireless Microphone Rechargeable UHF Dual Karaoke Mic with metal microphone Mini Ultra-compact Streaming Microphone Professional UHF Handheld 2pcs Wireless Microphone System with Receiver for PA/Karaoke/Vlogging/Podcasting",
          "ratings": [14,9,10,88,247],
          "stocks": 5156,
          "reorderlvl": 80,
          "sellingprice": 2600,
          "discount": 42,
          "isarchived": 0
        },
    ]

    i = 1
    for product in products:
        product['id'] = i
        i += 1
    
    print(products[0])

    context = {
        'products': products
    }
    return render(request, 'crms_app/pages/catalogProduct.html', context)



def searchPage(request):
    return render(request, 'crms_app/pages/searchPage.html')

def detailedProduct(request,pk):
    data = {}
    reviewForm = CustomerReviewForm()
    try:
        customer = AuthUser.objects.get(id=request.user.id)
        data["isRegistered"] = True
    except AuthUser.DoesNotExist:
        data["isRegistered"] = False
    product = Product.objects.get(id=pk)
    reviews = CustomerReview.objects.filter(product=product)
    reviewNum = len(reviews)
    print(reviews)
    print(reviewNum)
    mean_rating = 0
    if(reviewNum != 0):
        for review in reviews:
            mean_rating += review.rating
        mean_rating = mean_rating/reviewNum
    data['reviewNum'] = reviewNum
    data['reviews'] = reviews
    data["mean_rating"] = mean_rating

    if(request.method == "POST" and data.get("isRegistered")):
        review, created = CustomerReview.objects.get_or_create(customer=customer,product=product)
        reviewForm = CustomerReviewForm(request.POST, instance=review)
        if(reviewForm.is_valid()):
            reviewForm.save()
            messages.success(request, "The review was created on "+ product.name)
            return redirect(f"/crms/detailedProduct/{pk}")
    data['product'] = product
    data['reviewForm'] = reviewForm

    return render(request, 'crms_app/pages/detailedProduct.html', data)

def submitProductComplaint(request, pk):
    data = {}
    productComplaintForm = ProductComplaintForm()
    data["productComplaintForm"] = productComplaintForm
    try:
        customer = AuthUser.objects.get(id=request.user.id)
        data["isRegistered"] = True
    except AuthUser.DoesNotExist:
        data["isRegistered"] = False
    
    product = Product.objects.get(id=pk)
    data["product"] = product
    if(request.method == "POST" and data.get("isRegistered")):
        productComplaint, created = ProductComplaint.objects.get_or_create(customer=customer,product=product)
        productComplaintForm = ProductComplaintForm(request.POST, instance=productComplaint)
        if(productComplaintForm.is_valid()):
            productComplaintForm.save()
            messages.success(request, "A complaint was created on "+ product.name)
            return redirect(f"/crms/detailedProduct/{pk}")

    return render(request, 'crms_app/pages/submitProductComplaint.html',data)

def login_page(request):
    return render(request, 'crms_app/pages/login.html')

def passwordChange(request):
    return render(request, 'crms_app/pages/passwordChange.html')

def passwordForgot(request):
    return render(request, 'crms_app/pages/passwordForgot.html')

def register(request):
    return render(request, 'crms_app/pages/register.html')

# Customer Information
#CustomerInformation Page
@login_required(login_url=login_URL)
def customerInformation(request,pk):
    customer = AuthUser.objects.get(id=pk,user_type=2)
    customerInformation, created = CustomerInformation.objects.get_or_create(customer=customer)
    form = CustomerInformationUpdateForm(instance=customerInformation)
    if(request.method == "POST"):
        form = CustomerInformationUpdateForm(request.POST, instance=customer)
        if(form.is_valid()):
            form.save()
            return redirect("/crms/customerInformation/"+pk)
    data = {"form": form}
    return render(request, 'crms_app/Customer Information/customerInformation.html', data)


@login_required(login_url=login_URL)
def productComplaint(request,pk):
    customer = AuthUser.objects.get(id=pk, user_type=2)
    productComplaint, created = ProductComplaint.objects.get_or_create(customer=customer)
    data = {
        "productComplaint" : productComplaint,
        'created' : created,
    }
    return render(request, 'crms_app/Customer Information/productComplaint.html', data)

@login_required(login_url=login_URL)
def customerReview(request,pk):
    customer = AuthUser.objects.get(id=pk, user_type=2)
    customerReview, created = CustomerReview.objects.get_or_create(customer=customer)
    data = {
        "customerReview" : customerReview,
        'created' : created,
    }
    return render(request, 'crms_app/Customer Information/customerReview.html', data)


def removeReview(request, pk):
    review = CustomerReview.objects.get(id=pk)
    product = review.product
    review.delete()
    messages.success(request, "The review was removed on "+ product.name)
    return redirect(f"/crms/detailedProduct/{product.id}")




#OPTIONAL
def about(request):
    return render(request, 'crms_app/pages/about.html')

#TESTS
#CRUD
@login_required(login_url=login_URL)
def manageCustomers(request):
    #query
    customers = getCustomersList()
    customerInformations = []
    for customer in customers:
        customerInformations.append(getCustomerInformation(customer))
    # Gets all the customer information
    data = {"customers": customers,
            "customerInformations": customerInformations,
    }
    return render(request, 'crms_app/pages/manageCustomers.html', data)

def create(request):
    form = AuthUserCreationForm()
    if(request.method == "POST"):
        form = AuthUserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/crms/manageCustomers")

    data = {"form": form}
    return render(request, 'crms_app/CRUD/create.html', data)

def update(request,pk):
    customer = AuthUser.objects.get(id=pk,user_type=2)
    customerInformation, created = CustomerInformation.objects.get_or_create(customer=customer)
    form = CustomerInformationUpdateForm(instance=customerInformation)
    if(request.method == "POST"):
        form = CustomerInformationUpdateForm(request.POST, instance=customerInformation)
        if(form.is_valid()):
            form.save()
            return redirect("/crms/manageCustomers")
    data = {"form": form,
    "customerInformation": customerInformation,
    
    }
    return render(request, 'crms_app/CRUD/update.html', data)


def delete(request,pk):
    customer = AuthUser.objects.get(id=pk,user_type=2)
    customer.delete()
    return redirect("/crms/manageCustomers")






#REGISTER-LOGIN
def testRegister_page(request):
    form = AuthUserCreationForm()
    if( request.method == "POST"):
        form = AuthUserCreationForm(request.POST)
        if( form.is_valid() ):
            form.save()
            messages.success(request, "Account was created for "+form.cleaned_data.get("username"))
            return redirect('/crms/testLogin')

    data = {"form": form}
    return render(request, 'crms_app/TEST-Register-Login/test-register.html',data)


def testLogin_page(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        customer = authenticate(request, username=username, password=password)
        
        if customer is not None:
            login(request, customer)
            return redirect('/crms/')
        else:
            print("Login Fail.")
            messages.error(request, "Incorrect password or username.")


    return render(request, 'crms_app/TEST-Register-Login/test-login.html')


def testLogout_page(request):
    logout(request)
    return redirect('/crms/testLogin')


#Auxilliary functions
    #Create Functions

def getCustomersList():
    authUser = AuthUser.objects.filter(user_type=2)
    customers = []
    for customer in authUser:
        customers.append(customer)
    return customers

def getCustomerInformation(authUser):
    customerInformation, created = CustomerInformation.objects.get_or_create(customer=authUser)
    return customerInformation