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
        {
          "category": "menUpper",
          "name": "splicing cloth pure cotton polo shirt for mens",
          "ratings": [23,9,7,37,39],
          "stocks": 4839,
          "reorderlvl": 200,
          "sellingprice": 129,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Polo T shirt Yalex Red Label High Quality Unisex For Men",
          "ratings": [2,20,22,16,79],
          "stocks": 4039,
          "reorderlvl": 110,
          "sellingprice": 232,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "SOFTEX Polo shirt For Men and Women (Honeycomb) Unisex Plain",
          "ratings": [20,2,13,99,119],
          "stocks": 698,
          "reorderlvl": 60,
          "sellingprice": 250,
          "discount": 58,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Blue Corner Polo Shirt For Adult Mens Black",
          "ratings": [21,13,34,32,12],
          "stocks": 4901,
          "reorderlvl": 190,
          "sellingprice": 235,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Blue Corner Poloshirt with lining style #4",
          "ratings": [21,23,34,48,103],
          "stocks": 4365,
          "reorderlvl": 100,
          "sellingprice": 195,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "APPLE GREEN Polo Shirts For Men Casual Shirt Short sleeves with POLO Embroidery",
          "ratings": [4,14,6,49,236],
          "stocks": 931,
          "reorderlvl": 110,
          "sellingprice": 250,
          "discount": 33,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Splicing cloth pure cotton polo shirt for men’s",
          "ratings": [19,8,45,30,127],
          "stocks": 2613,
          "reorderlvl": 10,
          "sellingprice": 265,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "RTW Assorted Design OVS POLO for KIDS (1 piece only)",
          "ratings": [5,10,34,28,115],
          "stocks": 2528,
          "reorderlvl": 30,
          "sellingprice": 299,
          "discount": 67,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Polo Barong (Long sleeves) Cream",
          "ratings": [3,22,46,65,137],
          "stocks": 4889,
          "reorderlvl": 160,
          "sellingprice": 205,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Blue Corner Poloshirt with lining style #5",
          "ratings": [0,10,2,2,291],
          "stocks": 3560,
          "reorderlvl": 180,
          "sellingprice": 220,
          "discount": 10,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "LC 7 colors Men Regular Size  Casual Classic Solid Color Polo Shirts Cotton Short Sleeve comfortable sale cod .size s m l xl",
          "ratings": [8,7,14,97,292],
          "stocks": 3309,
          "reorderlvl": 170,
          "sellingprice": 999,
          "discount": 75,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Blue Corner Premium Cotton Men Penguin Red",
          "ratings": [2,1,20,25,22],
          "stocks": 1170,
          "reorderlvl": 120,
          "sellingprice": 1005,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Blue Corner POLOSHIRT WITH STRIPES (LINING) STYLE #4 For Men and Women (UNISEX)",
          "ratings": [8,6,40,47,248],
          "stocks": 3088,
          "reorderlvl": 140,
          "sellingprice": 280,
          "discount": 21,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Original Blue Corner Polo Shirt Men Unisex XS to 5XL White Black Gray",
          "ratings": [1,4,2,89,111],
          "stocks": 3434,
          "reorderlvl": 0,
          "sellingprice": 420,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Lifeline Polo shirt with collar Men's (Royal Blue)",
          "ratings": [4,16,2,73,169],
          "stocks": 2632,
          "reorderlvl": 130,
          "sellingprice": 222,
          "discount": 11,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "HUILISHI 9 COLOUR Chinese collar men's short-sleeved cotton shirt polo shirt",
          "ratings": [8,15,2,49,15],
          "stocks": 1438,
          "reorderlvl": 230,
          "sellingprice": 799,
          "discount": 69,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Original Blue Corner Polo Men's White (Polo Shirt Comfort Wear)",
          "ratings": [2,23,40,39,4],
          "stocks": 4574,
          "reorderlvl": 180,
          "sellingprice": 169,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Shirt On Yalex Plain Polo colored AQUA BLUE Shirt WITH COLLAR  Yalex Red Label High Quality Shirt Ideal for Printing as Uniform for School and Work Unisex Men and Women",
          "ratings": [12,15,20,60,7],
          "stocks": 4755,
          "reorderlvl": 180,
          "sellingprice": 249,
          "discount": 45,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Couple polo shirt stretch cotton (individual price)",
          "ratings": [17,19,5,31,132],
          "stocks": 5994,
          "reorderlvl": 130,
          "sellingprice": 250,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "SOFTEX Polo shirt For Men and Women (Honeycomb) Plain SHADES OF BLUE",
          "ratings": [13,18,2,32,250],
          "stocks": 2999,
          "reorderlvl": 80,
          "sellingprice": 200,
          "discount": 44,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "51Talk Bundles ( 51 Talk Polo Shirt, Lanyard, and Max Button Pin )",
          "ratings": [13,15,39,50,15],
          "stocks": 5853,
          "reorderlvl": 140,
          "sellingprice": 866,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "PING LACSON POLOSHIRT/TSHIRT FULL SUBLIMATION HIGH QUALITY",
          "ratings": [12,9,47,82,26],
          "stocks": 5310,
          "reorderlvl": 70,
          "sellingprice": 866,
          "discount": 54,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Yalex Colored AQUA BLUE POLO Shirt Plain Shirt For Printing School and Uniform Unisex Men and Women Yalex Gold",
          "ratings": [3,17,45,52,59],
          "stocks": 1841,
          "reorderlvl": 210,
          "sellingprice": 249,
          "discount": 41,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "cotton long sleeves  polo shirt for boy / men  for smart casual wear (white and colored variation available)",
          "ratings": [9,5,34,91,187],
          "stocks": 5065,
          "reorderlvl": 200,
          "sellingprice": 780,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "PROTECTION AGENT HIGH QUALITY FULL SUBLIMATION Poloshirt",
          "ratings": [5,6,44,97,51],
          "stocks": 3161,
          "reorderlvl": 10,
          "sellingprice": 999,
          "discount": 51,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "HUILISHI 9 COLOUR High quality Korean fashion plain men's casual shirt suitable for office and various occasions",
          "ratings": [4,18,49,98,282],
          "stocks": 4889,
          "reorderlvl": 230,
          "sellingprice": 599,
          "discount": 59,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Blue Corner Polo Shirt For Mens Adult White",
          "ratings": [3,4,28,64,32],
          "stocks": 4728,
          "reorderlvl": 200,
          "sellingprice": 665,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "POLO SHIRT ACID DARK GRAY PLAIN UNISEX (GOOD QUALITY CLOTHING)",
          "ratings": [6,11,31,32,230],
          "stocks": 2285,
          "reorderlvl": 100,
          "sellingprice": 190,
          "discount": 11,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Softex Light Color Honey Comb Polo Shirt Color Pink, Peach, Light Gold, Yellow Light Orange, Light Apple Green, Apple Green, Light Green, Light Blue, Sky Blue, Aqua Marine, Twisted Gray",
          "ratings": [9,14,47,81,148],
          "stocks": 3302,
          "reorderlvl": 210,
          "sellingprice": 750,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "HUILISHI Korean fashion casual pajama collar high quality striped polo shirt",
          "ratings": [24,16,39,17,131],
          "stocks": 2558,
          "reorderlvl": 70,
          "sellingprice": 899,
          "discount": 72,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "JL CLASSIC WEAR X HUILISHI CHINESE COLAR HIGH QUALITY SILK COTTON FABRIC SHORT SLEEVES POLO FULL BUTTON",
          "ratings": [6,23,6,58,252],
          "stocks": 4503,
          "reorderlvl": 50,
          "sellingprice": 1199,
          "discount": 78,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "51Talk New Bundle ( 51 Talk Polo Shirt, Latest 2021 Design Lanyard, and Max Button Pin )",
          "ratings": [12,17,14,90,131],
          "stocks": 3706,
          "reorderlvl": 240,
          "sellingprice": 310,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Plain Polo Shirt: Softex/Southport Honeycomb UNISEX COLORED yellow gold / violet / ube/ sunkist / orange",
          "ratings": [4,18,9,17,173],
          "stocks": 5437,
          "reorderlvl": 0,
          "sellingprice": 280,
          "discount": 54,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "Blue Corner POLOSHIRT WITH STRIPES (LINING) STYLE #10 For Men and Women (UNISEX)",
          "ratings": [9,15,12,98,21],
          "stocks": 2490,
          "reorderlvl": 210,
          "sellingprice": 350,
          "discount": 29,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "HUILISHI High quality multi-style design Hawaiian short sleeve men's pol shirt",
          "ratings": [5,6,18,30,182],
          "stocks": 1692,
          "reorderlvl": 220,
          "sellingprice": 589,
          "discount": 67,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "HUILISHI Microfiber polo T-shirt striped summer top lapel short sleeve men's polo shirt S-XL",
          "ratings": [25,14,4,71,285],
          "stocks": 3445,
          "reorderlvl": 180,
          "sellingprice": 599,
          "discount": 61,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "i-tech Honeycomb Polo Shirt Professional ,Casual and breathable apparel for Men and Women",
          "ratings": [21,9,46,84,249],
          "stocks": 514,
          "reorderlvl": 80,
          "sellingprice": 199,
          "discount": 6,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "HUILISHI 5 COLOUR Chinese collar men's short-sleeved cotton shirt polo shirt",
          "ratings": [1,4,42,73,111],
          "stocks": 4048,
          "reorderlvl": 220,
          "sellingprice": 799,
          "discount": 69,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "5 COLOUR ANCHOR OR LEAVES PRINT COTTON SHORT SLEEVE  MENS POLO FOR HUILISHI.ph",
          "ratings": [13,11,3,33,128],
          "stocks": 900,
          "reorderlvl": 80,
          "sellingprice": 599,
          "discount": 60,
          "isarchived": 0
        },
        {
          "category": "menUpper",
          "name": "SOFTEX Polo shirt For Men and Women (Honeycomb) Plain YELLOW ORANGE VIOLET",
          "ratings": [20,25,31,21,74],
          "stocks": 5133,
          "reorderlvl": 180,
          "sellingprice": 200,
          "discount": 44,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "OneFamily Plain Jogger Pants Makapal Tela 20+ Colors High Quality",
          "ratings": [1,1,9,95,57],
          "stocks": 1501,
          "reorderlvl": 110,
          "sellingprice": 199,
          "discount": 55,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "Unisex plain Jogger pants cotton ins hot JF01",
          "ratings": [4,15,24,31,114],
          "stocks": 3551,
          "reorderlvl": 110,
          "sellingprice": 598,
          "discount": 86,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "Agila Air Cool Sport Shorts",
          "ratings": [3,11,6,80,38],
          "stocks": 2859,
          "reorderlvl": 20,
          "sellingprice": 200,
          "discount": 31,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "☁  Qc PROMO Koko AGAM The Latest Cheapest Jumbo Koko Muslim Dress For Men",
          "ratings": [23,21,26,40,152],
          "stocks": 3546,
          "reorderlvl": 140,
          "sellingprice": 1552,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "MPJ Cargo Pants multi-pocket pants with Zipper Pocket 2022 NewStyle HighQuality Pants",
          "ratings": [10,23,35,59,146],
          "stocks": 3585,
          "reorderlvl": 200,
          "sellingprice": 1599,
          "discount": 81,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "JF229 High Quality Camouflage Cotton Jogger Pants For Him- Magic Fashion Jeans",
          "ratings": [16,18,20,31,20],
          "stocks": 3117,
          "reorderlvl": 70,
          "sellingprice": 598,
          "discount": 75,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "Tree line two pocket plain jogger pants for unisex",
          "ratings": [8,23,8,46,253],
          "stocks": 4429,
          "reorderlvl": 50,
          "sellingprice": 265,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "KingJames Unisex Plain Tiro Korean Sports Jogger Pants",
          "ratings": [23,15,14,87,84],
          "stocks": 5315,
          "reorderlvl": 160,
          "sellingprice": 500,
          "discount": 87,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "COD New Comfortable Men’s Soft Pranela Pajama 1pc",
          "ratings": [24,2,11,22,99],
          "stocks": 1576,
          "reorderlvl": 120,
          "sellingprice": 89,
          "discount": 37,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "Cargo shorts four pocket with belt #1923",
          "ratings": [13,15,3,10,258],
          "stocks": 5436,
          "reorderlvl": 110,
          "sellingprice": 299,
          "discount": 33,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "BEST SELLING FASHIONABLE 011# PLAIN JOGGER PANTS FOR MEN",
          "ratings": [14,7,16,30,18],
          "stocks": 5916,
          "reorderlvl": 240,
          "sellingprice": 645,
          "discount": 80,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "Two Toned Jogger Pants  Dazzling and Marvelous Street Wear Niike JB28-5 [[[FJ FASHION]]]",
          "ratings": [11,15,6,42,186],
          "stocks": 516,
          "reorderlvl": 140,
          "sellingprice": 199,
          "discount": 60,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "TWO new casual sweatpants three lines jogger pants/cotton pants unisex cod（9848#）",
          "ratings": [6,17,25,92,13],
          "stocks": 3762,
          "reorderlvl": 220,
          "sellingprice": 300,
          "discount": 60,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "NEW TREND HIGH QUALITY JL CLASSIC WEAR FREE SHIPPING 5 COLOR SLACKS ANKLE CUT KOREAN STYLE FORMAL ATTIRE WITH POCKET FIT UP TO SIZE 36 INCHES WAISTLINE",
          "ratings": [23,13,42,8,27],
          "stocks": 824,
          "reorderlvl": 80,
          "sellingprice": 1199,
          "discount": 80,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "Plain tiro Korean Sports Plain jogger#AJ PH SHOP",
          "ratings": [8,7,8,83,170],
          "stocks": 2071,
          "reorderlvl": 190,
          "sellingprice": 600,
          "discount": 88,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "H&T Mens Jogger pants zipper with pocket  Unisex Makapal tela",
          "ratings": [5,19,15,96,133],
          "stocks": 3331,
          "reorderlvl": 10,
          "sellingprice": 599,
          "discount": 84,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "Plain Jogger pants for unisex",
          "ratings": [11,2,13,26,89],
          "stocks": 5853,
          "reorderlvl": 220,
          "sellingprice": 385,
          "discount": 83,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "YATO 3lines unisex plain cotton jogging pants with zipper stretchable",
          "ratings": [9,24,15,69,238],
          "stocks": 3373,
          "reorderlvl": 140,
          "sellingprice": 189,
          "discount": 42,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "new)Slacks for men/SKINNY TYPE/uniform",
          "ratings": [16,14,17,62,252],
          "stocks": 5483,
          "reorderlvl": 50,
          "sellingprice": 500,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "#JF10 New Trendy Jogger Pants Fashionable & Comfortable For Men 4Colors COD",
          "ratings": [5,6,22,73,10],
          "stocks": 1107,
          "reorderlvl": 60,
          "sellingprice": 1299,
          "discount": 92,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "Men's  slacks black for formal,office,school and  wedding pants in skinny fit!!",
          "ratings": [12,8,36,58,32],
          "stocks": 4174,
          "reorderlvl": 190,
          "sellingprice": 1000,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "JOGGER PANTS KIDS 1-12YRS OLD S-M-L-XL TERRY BRUSH FABRICS",
          "ratings": [5,20,39,34,298],
          "stocks": 4093,
          "reorderlvl": 20,
          "sellingprice": 250,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "MYS FASHION CLUB Jogging Pants For Men/New Arrival/Good Quality/Fashion/Cotton/Bestseller",
          "ratings": [9,16,18,12,179],
          "stocks": 445,
          "reorderlvl": 40,
          "sellingprice": 249,
          "discount": 56,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "Inmodoo Unisex Cotton Plain Jogger Pants Zipper Joggers Sweats",
          "ratings": [25,12,47,17,280],
          "stocks": 4620,
          "reorderlvl": 190,
          "sellingprice": 599,
          "discount": 82,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "Checkered Franella Pants Plaid Loose Straight High Waist wide leg",
          "ratings": [18,23,46,55,36],
          "stocks": 1557,
          "reorderlvl": 40,
          "sellingprice": 250,
          "discount": 48,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "YATO Unisex G.A.P Jogger Pants Makapal Tela",
          "ratings": [17,7,27,97,76],
          "stocks": 3634,
          "reorderlvl": 220,
          "sellingprice": 189,
          "discount": 38,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "Camouflage Pants for Lalaki Military uniforms men's straight 6 pocket pants hip-hop pants pocket pants men's overalls casual camouflage pants long pants Coumflage Trousers",
          "ratings": [10,24,30,96,138],
          "stocks": 4726,
          "reorderlvl": 120,
          "sellingprice": 3599,
          "discount": 93,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "SAMAHANG ILOCANO Fraternity Jogger",
          "ratings": [15,2,5,73,243],
          "stocks": 3131,
          "reorderlvl": 30,
          "sellingprice": 185,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "security guard pants navy blue gabardine",
          "ratings": [16,3,15,85,88],
          "stocks": 1083,
          "reorderlvl": 180,
          "sellingprice": 150,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "YATO Men's Letter Print Sweatpants Fashion Jogging Pants Men",
          "ratings": [17,13,9,15,218],
          "stocks": 610,
          "reorderlvl": 130,
          "sellingprice": 199,
          "discount": 21,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "New Pants  working Pangtrabaho Pants with pocket Adult",
          "ratings": [21,8,45,75,15],
          "stocks": 3946,
          "reorderlvl": 50,
          "sellingprice": 95,
          "discount": 42,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "unisex jogger 100clover king james23",
          "ratings": [17,19,0,44,290],
          "stocks": 4738,
          "reorderlvl": 180,
          "sellingprice": 850,
          "discount": 88,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "UNIFIT  Men's Dri Fit Jogger Pants Casual Walker Training Sports Jogging Fitness & Lifestyles UF-012",
          "ratings": [9,8,30,95,102],
          "stocks": 5718,
          "reorderlvl": 140,
          "sellingprice": 65,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "security guard pants navy blue",
          "ratings": [18,15,35,100,179],
          "stocks": 5569,
          "reorderlvl": 200,
          "sellingprice": 105,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "PAJAMA CHECKERD 2XL SIZE (36-42)",
          "ratings": [17,10,33,23,75],
          "stocks": 3632,
          "reorderlvl": 190,
          "sellingprice": 522,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "JOGGING PANTS (free size fit meduim to large)",
          "ratings": [13,17,21,3,90],
          "stocks": 924,
          "reorderlvl": 140,
          "sellingprice": 79,
          "discount": 1,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "MPJ Khaki Plain Man Pants ArmyGreen Grey Trousers Uniform",
          "ratings": [7,2,10,71,166],
          "stocks": 1526,
          "reorderlvl": 0,
          "sellingprice": 599,
          "discount": 55,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "jogger pants for women unisex track pants sweat pants for womens sweatpants joggers TikTok pants",
          "ratings": [9,2,31,9,186],
          "stocks": 5358,
          "reorderlvl": 30,
          "sellingprice": 156,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "YATO UNISEX TASLAN DRAPE JOGGER PANTS",
          "ratings": [17,2,49,41,57],
          "stocks": 346,
          "reorderlvl": 180,
          "sellingprice": 298,
          "discount": 44,
          "isarchived": 0
        },
        {
          "category": "menLower",
          "name": "jogger pants for kids (1 to 12yrs old)",
          "ratings": [10,9,33,9,233],
          "stocks": 4830,
          "reorderlvl": 10,
          "sellingprice": 75,
          "discount": 35,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Girl Scout Active Wear Black Polo Shirt for Adult Members",
          "ratings": [1,25,32,84,253],
          "stocks": 808,
          "reorderlvl": 130,
          "sellingprice": 265,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "JDN - COMBI MESH OVERSIZED SHIRT - FIT TO MEDIUM-3XL",
          "ratings": [13,8,39,63,21],
          "stocks": 5251,
          "reorderlvl": 160,
          "sellingprice": 230,
          "discount": 31,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "ZENAB: Kristop off-Shoulder Plain Blouse For Womens/Ladies High Quality Cotton Spandex Fabric Fit Small to Large",
          "ratings": [16,2,30,80,166],
          "stocks": 1894,
          "reorderlvl": 40,
          "sellingprice": 499,
          "discount": 74,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "SALE!! SALE!! SALE!! COD KOREAN FASHION DESIGN MALL PULL OUTS ASSORTED CROPTOP BLOUSES PURE COTTON (ASSORTED DESIGNS ONLY)  PROMO!!!",
          "ratings": [8,9,2,16,248],
          "stocks": 1707,
          "reorderlvl": 80,
          "sellingprice": 499,
          "discount": 93,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Sex Jazz Girl Print Design T-shirt for women Round neck  Tops",
          "ratings": [21,22,24,72,209],
          "stocks": 3732,
          "reorderlvl": 70,
          "sellingprice": 196,
          "discount": 75,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "UA men's T-shirt 2022 new UA sports running short-sleeved top 1361130",
          "ratings": [20,19,17,7,167],
          "stocks": 4422,
          "reorderlvl": 0,
          "sellingprice": 2,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Unisex T-Shirt Chibi Tees BTS BT21 Tees Cartoons Cute Tees COD pure Cotton",
          "ratings": [22,18,12,90,33],
          "stocks": 2167,
          "reorderlvl": 220,
          "sellingprice": 249.99,
          "discount": 74,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "GUITAR LADIE'S POLO SHIRT RED",
          "ratings": [14,19,31,61,120],
          "stocks": 4131,
          "reorderlvl": 170,
          "sellingprice": 320,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Men's adult plain basic sando",
          "ratings": [16,24,20,28,186],
          "stocks": 4034,
          "reorderlvl": 200,
          "sellingprice": 700,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "JB71 New Fashionable Sexy BRALETTE Good Quality- FASHION JEANS LION",
          "ratings": [16,5,14,18,16],
          "stocks": 3364,
          "reorderlvl": 230,
          "sellingprice": 299,
          "discount": 90,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Shirtista I LOVE TACLOBAN CITYWomen's T-Shirt (Navy Blue)",
          "ratings": [16,13,3,19,74],
          "stocks": 2533,
          "reorderlvl": 210,
          "sellingprice": 420,
          "discount": 7,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "New Print!! Yassie 2 way puff dress/s-large/crepe",
          "ratings": [14,11,35,0,244],
          "stocks": 973,
          "reorderlvl": 110,
          "sellingprice": 350,
          "discount": 37,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Leni Kiko 2022 Trendy Graphic Tees for Kids to Adult",
          "ratings": [18,19,47,45,172],
          "stocks": 4901,
          "reorderlvl": 30,
          "sellingprice": 525,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Child Development Worker  shirt",
          "ratings": [15,9,27,67,159],
          "stocks": 962,
          "reorderlvl": 50,
          "sellingprice": 538,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "myfaithshop Zumba Quality drifit men women unisex fashion casual t-shirt tshirt short sleeve round neck comfy summer couple",
          "ratings": [8,19,49,27,261],
          "stocks": 4263,
          "reorderlvl": 240,
          "sellingprice": 339,
          "discount": 53,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Blue Corner Ladies Polo Shirt Plain Comfort Wear Azalea",
          "ratings": [16,20,18,35,34],
          "stocks": 5383,
          "reorderlvl": 150,
          "sellingprice": 399,
          "discount": 47,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Blue Corner Ladies Polo Shirt Plain Comfort Wear Lemon Chrome",
          "ratings": [22,4,50,48,77],
          "stocks": 2864,
          "reorderlvl": 130,
          "sellingprice": 399,
          "discount": 47,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Tees Ladies tshirt printed graphic tee t shirt shirts tshirts for Women womens sale #T-20023-20027",
          "ratings": [12,2,44,74,264],
          "stocks": 346,
          "reorderlvl": 180,
          "sellingprice": 196,
          "discount": 70,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Zumba Shirt Wear Women Fitness White Top Lover Tshirt Urban Female Short Sleeve Fashion Tee Rainbow Spain Free Shipping Yeskuni",
          "ratings": [5,7,33,9,171],
          "stocks": 4907,
          "reorderlvl": 100,
          "sellingprice": 456,
          "discount": 61,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "A&C #12PCS #03-B PANTY WOMENS UNDERWER COTTON",
          "ratings": [13,25,50,35,119],
          "stocks": 5117,
          "reorderlvl": 20,
          "sellingprice": 550,
          "discount": 71,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "TaylorMade UA PING pxg new golf clothing women's short-sleeved T-shirt summer GOLF sports slim breathable quick-drying clothes POLO shirt",
          "ratings": [21,21,7,75,38],
          "stocks": 3496,
          "reorderlvl": 190,
          "sellingprice": 2,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Blue Corner Ladies Polo Shirt Plain Comfort Wear Choco Brown",
          "ratings": [22,11,43,68,140],
          "stocks": 4679,
          "reorderlvl": 120,
          "sellingprice": 399,
          "discount": 47,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "DIY T-Shirt Design for Men and Women",
          "ratings": [7,1,46,3,58],
          "stocks": 4693,
          "reorderlvl": 180,
          "sellingprice": 169,
          "discount": 41,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "COCOMELON SHIRT for kids",
          "ratings": [20,8,26,68,83],
          "stocks": 2883,
          "reorderlvl": 50,
          "sellingprice": 425,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "[GEEBERRY] COOL COUPLE TSHIRT II GRAPHIC TEES II SOLD PER PIECE",
          "ratings": [4,4,47,63,289],
          "stocks": 3024,
          "reorderlvl": 240,
          "sellingprice": 325,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Nacho Varga Casual TShirt Better Call Saul Jimmy McGill Creative Tops 4XL 5XLLeisure T Shirt Girl Short Sleeve Unique Gift Idea",
          "ratings": [9,13,36,88,187],
          "stocks": 2225,
          "reorderlvl": 60,
          "sellingprice": 599,
          "discount": 70,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "RL# Korean Fahion  Cap For Woman and Man",
          "ratings": [15,21,20,26,42],
          "stocks": 4245,
          "reorderlvl": 200,
          "sellingprice": 250,
          "discount": 73,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "White Shirt Unisex ( FOR MEN AND WOMEN)",
          "ratings": [24,9,27,49,1],
          "stocks": 3536,
          "reorderlvl": 170,
          "sellingprice": 200,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Sublimation crop top #3",
          "ratings": [25,7,23,2,237],
          "stocks": 4249,
          "reorderlvl": 40,
          "sellingprice": 60,
          "discount": 18,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "AFFORB Tube Binder / Supporter",
          "ratings": [21,24,12,11,165],
          "stocks": 3825,
          "reorderlvl": 120,
          "sellingprice": 500,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Team Jesus Christian T-shirt gospel shirt verse",
          "ratings": [11,7,23,46,192],
          "stocks": 2305,
          "reorderlvl": 140,
          "sellingprice": 199,
          "discount": 20,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "3PCs Plus Size Women's Tank Top",
          "ratings": [5,17,46,79,269],
          "stocks": 1032,
          "reorderlvl": 140,
          "sellingprice": 500,
          "discount": 66,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Ruidiandian Knitted Sweater Ladies T-shirt 2021 Summer New Silk Sunscreen Women Korean Fashion Loose All-match Jacket Hollow",
          "ratings": [23,8,5,78,147],
          "stocks": 2247,
          "reorderlvl": 140,
          "sellingprice": 300,
          "discount": 45,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Women’s Polo Poloshirt",
          "ratings": [0,16,3,21,173],
          "stocks": 404,
          "reorderlvl": 180,
          "sellingprice": 499,
          "discount": 60,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "JFK Chill Korean Graphic Statement T-Shirt for Women",
          "ratings": [13,21,0,28,229],
          "stocks": 1210,
          "reorderlvl": 90,
          "sellingprice": 129,
          "discount": 54,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "RA190-2# 6 PCS PANTY WOMENS COTTON",
          "ratings": [18,13,37,31,99],
          "stocks": 2585,
          "reorderlvl": 230,
          "sellingprice": 250,
          "discount": 68,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "High-quality cotton, large size, fashion printing, couple styles o507s",
          "ratings": [3,4,43,21,14],
          "stocks": 1158,
          "reorderlvl": 180,
          "sellingprice": 129,
          "discount": 33,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Genuine sports t-shirt UA men's fitness quick-drying summer new breathable short-sleeved",
          "ratings": [8,2,47,68,142],
          "stocks": 5705,
          "reorderlvl": 140,
          "sellingprice": 2,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "Maycaur Fashion Love Zumba Dance Print T Shirt Women Clothes Funny Graphic Printed Tshirt Femme Harajuku Shirt Hip Hop T-shirts",
          "ratings": [14,22,15,94,225],
          "stocks": 4900,
          "reorderlvl": 80,
          "sellingprice": 456,
          "discount": 61,
          "isarchived": 0
        },
        {
          "category": "womenUpper",
          "name": "T-neck croptop❣️",
          "ratings": [21,14,3,20,6],
          "stocks": 4037,
          "reorderlvl": 160,
          "sellingprice": 100,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Regatta Skort For Women (Light Blue)",
          "ratings": [19,2,14,2,73],
          "stocks": 3921,
          "reorderlvl": 10,
          "sellingprice": 322,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Vampire Crisscross Mini Skirt Plain Design 19A0038",
          "ratings": [7,21,48,76,224],
          "stocks": 988,
          "reorderlvl": 150,
          "sellingprice": 200,
          "discount": 78,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Chafani MAXY  Latest MAXY DRESS Women  DENIM09",
          "ratings": [14,10,4,98,276],
          "stocks": 772,
          "reorderlvl": 250,
          "sellingprice": 3670,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Korean version of high-waisted white short skirt fashion sexy a-line pleated mini tennis skirt",
          "ratings": [4,8,30,44,93],
          "stocks": 3938,
          "reorderlvl": 240,
          "sellingprice": 588,
          "discount": 73,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "LOTUS 600W Electric Wood Planer for Woodworking 580W LTPL5800 82mm •BUILDMATE• LPT lutos",
          "ratings": [1,17,15,74,87],
          "stocks": 4774,
          "reorderlvl": 110,
          "sellingprice": 2497,
          "discount": 40,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "SHEIN Elastic Waist Back Snap Skirt (with etiketa)",
          "ratings": [12,15,40,48,187],
          "stocks": 5761,
          "reorderlvl": 190,
          "sellingprice": 250,
          "discount": 26,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "COD 88# Korean style mini skirt Small size 25-29cm",
          "ratings": [3,24,9,24,115],
          "stocks": 5953,
          "reorderlvl": 120,
          "sellingprice": 150,
          "discount": 81,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Best Seller Jessie Ruffles Top  Skirt Dress Sexy Terno (BEST SELLER DRESS)(BSD)",
          "ratings": [5,14,44,56,247],
          "stocks": 3159,
          "reorderlvl": 30,
          "sellingprice": 828,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Semi Bodycon Skorts Skirt For Women Palda",
          "ratings": [14,4,9,27,131],
          "stocks": 888,
          "reorderlvl": 120,
          "sellingprice": 299,
          "discount": 81,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "PLUS SIZE BELOW THE KNEE PENCIL SKIRT (Free Size: Can fit 33-38in waistline)",
          "ratings": [3,10,46,63,7],
          "stocks": 5409,
          "reorderlvl": 190,
          "sellingprice": 522,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Buy 1 take 1 Plus size halter dress challis fabric",
          "ratings": [16,8,24,32,217],
          "stocks": 2978,
          "reorderlvl": 130,
          "sellingprice": 600,
          "discount": 55,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "OLGA Ditsy Summer High Waist Slit Floral Midi Skirt",
          "ratings": [5,1,10,97,118],
          "stocks": 2071,
          "reorderlvl": 210,
          "sellingprice": 149,
          "discount": 63,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "MO&CO Half-length skirt female new pleated skirt student Korean style high waist all-match short skirt A-line tie skirt",
          "ratings": [7,2,4,44,217],
          "stocks": 5299,
          "reorderlvl": 220,
          "sellingprice": 400,
          "discount": 63,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Cotton orihinal na pampanitikan retro na naka-print na palda pambabae sa tag-araw na bagong drape na maluwag malaking sukat slim a-line na palda 53",
          "ratings": [13,9,20,96,207],
          "stocks": 1284,
          "reorderlvl": 250,
          "sellingprice": 400,
          "discount": 75,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "[Ready Stock]  Automatic Tent Outdoor Tent 4-5 Person Tent For Camping Tent Waterproof",
          "ratings": [4,3,19,70,66],
          "stocks": 4984,
          "reorderlvl": 50,
          "sellingprice": 1143,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Retro oil painting style palda pambabae summer new all-match thin mid-length malaking sukat high waist a-line skirt 75",
          "ratings": [10,2,5,23,143],
          "stocks": 491,
          "reorderlvl": 10,
          "sellingprice": 400,
          "discount": 75,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "3PCS HALF SLIP / MIDI FOR WOMEN INNER COTTON SKIRT GIRLS LADIES ADULT WHITE SKIRTS HALFSLIP BELOW ABOVE KNEE",
          "ratings": [1,17,28,6,134],
          "stocks": 4611,
          "reorderlvl": 100,
          "sellingprice": 74,
          "discount": 1,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Fashion CRISSCROSS Skirt with SHEIIN PL4",
          "ratings": [7,25,37,74,224],
          "stocks": 807,
          "reorderlvl": 80,
          "sellingprice": 299,
          "discount": 82,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "2021 bagong high waist na palda maluwag at manipis na damit ng tag-init na may malaking sukat na pambabae mm180 catties temperament maikling palda net yarn flower 31",
          "ratings": [7,22,28,7,162],
          "stocks": 5721,
          "reorderlvl": 240,
          "sellingprice": 380,
          "discount": 79,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Maong Skirt & Higwaist Denim Skirt 3colors",
          "ratings": [17,13,13,35,243],
          "stocks": 5060,
          "reorderlvl": 100,
          "sellingprice": 480,
          "discount": 64,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Korean new plain falbala loose dress 4Colors",
          "ratings": [4,16,31,21,178],
          "stocks": 3014,
          "reorderlvl": 210,
          "sellingprice": 458,
          "discount": 2,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "korean Big size skirt for womens",
          "ratings": [15,5,12,9,220],
          "stocks": 4472,
          "reorderlvl": 190,
          "sellingprice": 250,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "PLUS SIZE PRINTED MINI SKIRT! SALE!",
          "ratings": [6,4,19,49,224],
          "stocks": 1256,
          "reorderlvl": 150,
          "sellingprice": 160,
          "discount": 63,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Genuine Leather Jazz Dance Shoes New Sneakers Dancing Shoes For Women Men Black Tan Pink Colors Sports Ballet Jazz Dance Shoes - Dance Shoes - AliExpress",
          "ratings": [5,13,29,74,182],
          "stocks": 1897,
          "reorderlvl": 0,
          "sellingprice": 1525,
          "discount": 49,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "39-45” Waistline Plain & Printed Plus Size Pencil Skirt",
          "ratings": [17,16,10,6,245],
          "stocks": 2012,
          "reorderlvl": 100,
          "sellingprice": 135,
          "discount": 4,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Printed Pleated Skirt",
          "ratings": [0,20,10,82,66],
          "stocks": 622,
          "reorderlvl": 210,
          "sellingprice": 906,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Huaerfei  Strechable Mini Skirt Casual Attire (Q69)",
          "ratings": [13,23,3,88,73],
          "stocks": 3208,
          "reorderlvl": 10,
          "sellingprice": 321,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "☆DIKE☆ Korean Fashion Women's High Waist Skirt Slim Pleated Skating Tennis School Skirt with Pleated Skirt",
          "ratings": [5,7,48,75,190],
          "stocks": 722,
          "reorderlvl": 100,
          "sellingprice": 500,
          "discount": 80,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "american terno boho terno party(top+floral skirt）",
          "ratings": [12,24,34,75,215],
          "stocks": 1445,
          "reorderlvl": 0,
          "sellingprice": 650,
          "discount": 74,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Jumper buckles skirt no inner",
          "ratings": [1,5,41,79,280],
          "stocks": 5123,
          "reorderlvl": 180,
          "sellingprice": 300,
          "discount": 44,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "❈ ZARA overrun denim skirt (blackwhitegray)",
          "ratings": [3,2,47,73,199],
          "stocks": 766,
          "reorderlvl": 110,
          "sellingprice": 159,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "SKIRT FREESIZE Korean style",
          "ratings": [23,18,36,99,262],
          "stocks": 1575,
          "reorderlvl": 50,
          "sellingprice": 266,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Student Uniform Cute Maid Dress Girls Cheerleader Costume Woman Anime Cosplay Party Costumes Women dress",
          "ratings": [18,18,34,23,18],
          "stocks": 3370,
          "reorderlvl": 70,
          "sellingprice": 228,
          "discount": 44,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "40KG (Red) 2in1 Dumbbell Dumbbell Set men and women fitness With Long Bar and Free Palm WristGuard",
          "ratings": [9,9,33,7,108],
          "stocks": 2315,
          "reorderlvl": 130,
          "sellingprice": 302,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "plus size/over size/denim skirt/below the knee/stretchable/fit 31to38waistline/high quality",
          "ratings": [20,24,43,47,27],
          "stocks": 2283,
          "reorderlvl": 210,
          "sellingprice": 250,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Crew Shorts",
          "ratings": [14,1,0,65,52],
          "stocks": 2912,
          "reorderlvl": 130,
          "sellingprice": 200,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "AOLINA 2022 summer new short skirt retro printing women's high waist thin a-line skirt anti-shine bag hip skirt",
          "ratings": [2,18,44,33,193],
          "stocks": 1439,
          "reorderlvl": 10,
          "sellingprice": 1095,
          "discount": 43,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "RHINESTONE DRESS fits up to 2XL",
          "ratings": [14,16,16,4,168],
          "stocks": 5839,
          "reorderlvl": 200,
          "sellingprice": 631,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "Fashion【Ready Stock】 Alisya Set of Jilbab instant sukob",
          "ratings": [5,20,39,82,218],
          "stocks": 2153,
          "reorderlvl": 20,
          "sellingprice": 1657,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "womenLower",
          "name": "SUNBOYZ Fashion  CRISSCROSS Skirt with SHEIIN Etiketa",
          "ratings": [2,19,7,94,65],
          "stocks": 805,
          "reorderlvl": 230,
          "sellingprice": 89,
          "discount": 34,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "COD NEW Underwear Men's Brief Assorted Color 3pcs per box",
          "ratings": [15,19,28,97,202],
          "stocks": 5580,
          "reorderlvl": 140,
          "sellingprice": 99,
          "discount": 25,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "COD 5 Colors New Style Cotton Boxer Briefs  For Men Underwear Super Stretchable Size:28inch-33inch",
          "ratings": [3,7,31,16,16],
          "stocks": 2211,
          "reorderlvl": 20,
          "sellingprice": 99,
          "discount": 66,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "Munafie Boxer brief spandex",
          "ratings": [19,4,24,35,3],
          "stocks": 3165,
          "reorderlvl": 180,
          "sellingprice": 60,
          "discount": 52,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "Puritan Men's Hipster Brief 531 White Pack of 3",
          "ratings": [2,23,21,30,59],
          "stocks": 4660,
          "reorderlvl": 40,
          "sellingprice": 300,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "COD Blalablala Underpants plain  ladies Panty 1pcs",
          "ratings": [20,18,48,65,236],
          "stocks": 645,
          "reorderlvl": 160,
          "sellingprice": 299,
          "discount": 97,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "Y&L Fashion #25NX High Quality 100% Cotton Boxer Brief For Men",
          "ratings": [21,4,9,96,6],
          "stocks": 3194,
          "reorderlvl": 70,
          "sellingprice": 90,
          "discount": 33,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "COD Underwear Brief Assorted Brand Random Color (1PC) Regular Size",
          "ratings": [15,4,24,88,299],
          "stocks": 1588,
          "reorderlvl": 190,
          "sellingprice": 25,
          "discount": 32,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "(1 piece) RESTOCK Unisex Underwear Cotton Boxer Shorts - RANDOM DESIGNS ONLY",
          "ratings": [8,16,27,27,17],
          "stocks": 5395,
          "reorderlvl": 50,
          "sellingprice": 75,
          "discount": 41,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "Umiwear Munafie Men's Underwear Men's Briefs Premium Brief For Men",
          "ratings": [20,2,23,2,70],
          "stocks": 745,
          "reorderlvl": 80,
          "sellingprice": 100,
          "discount": 72,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "6 PCS 100%cotton stretch BOXERS MENS",
          "ratings": [16,24,35,2,121],
          "stocks": 2531,
          "reorderlvl": 90,
          "sellingprice": 500,
          "discount": 63,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "MUNAFIE Brief boxer Seamless for Men",
          "ratings": [15,1,45,38,14],
          "stocks": 1648,
          "reorderlvl": 20,
          "sellingprice": 100,
          "discount": 65,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "KingJames 1Pcs Korean basic Boxer shorts",
          "ratings": [6,25,29,13,276],
          "stocks": 3826,
          "reorderlvl": 240,
          "sellingprice": 100,
          "discount": 80,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "COD Fashion men's spandex boxer briefs 6pcs/pack",
          "ratings": [10,20,39,61,121],
          "stocks": 5868,
          "reorderlvl": 40,
          "sellingprice": 399,
          "discount": 56,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "Men's Cotton Boxer Short With Button Placket",
          "ratings": [20,9,35,95,59],
          "stocks": 2142,
          "reorderlvl": 40,
          "sellingprice": 99,
          "discount": 52,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "COD Regular Size Underwear Brief Assorted Brand Random Color (1PC)",
          "ratings": [19,19,19,80,142],
          "stocks": 3703,
          "reorderlvl": 110,
          "sellingprice": 25,
          "discount": 32,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "6pcs Assorted color brief for men SALE!",
          "ratings": [12,7,20,58,43],
          "stocks": 5077,
          "reorderlvl": 30,
          "sellingprice": 199,
          "discount": 52,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "AAA Magic Magnetism Pants High-End Men's Underwear Seamless Suction Free Size Boxer Breathable Boxer Men's Underwear Seamless",
          "ratings": [2,3,21,44,5],
          "stocks": 1449,
          "reorderlvl": 210,
          "sellingprice": 299,
          "discount": 90,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "AM COD 6Pieces Men's 100% Cotton Brief  Underwear New",
          "ratings": [16,11,46,92,279],
          "stocks": 3121,
          "reorderlvl": 50,
          "sellingprice": 150,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "COD pcs/12pcs men's cotton high-quality fashion underwear underwear men's summer thin breathable shorts plus size pants",
          "ratings": [3,0,27,62,87],
          "stocks": 748,
          "reorderlvl": 180,
          "sellingprice": 399,
          "discount": 68,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "COD Emperor Men's 100% Cotton Boxer Short High Quality",
          "ratings": [14,17,2,93,254],
          "stocks": 1415,
          "reorderlvl": 80,
          "sellingprice": 99,
          "discount": 53,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "COD men's Cotton high-quality fashion Briefs Underwear 6pcs 1pack",
          "ratings": [19,12,49,65,206],
          "stocks": 4809,
          "reorderlvl": 170,
          "sellingprice": 299,
          "discount": 63,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "R005-430# 6 PCS 100%cotton stretch BOXERS MEN PLAIN GOOD QUALITY",
          "ratings": [5,14,40,48,6],
          "stocks": 2862,
          "reorderlvl": 30,
          "sellingprice": 500,
          "discount": 52,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "COD☑️Men's Boxer Underpants Seamless Breathable Middle Waist Underwear Free Size Boxer Briefs",
          "ratings": [1,19,40,45,56],
          "stocks": 566,
          "reorderlvl": 110,
          "sellingprice": 140,
          "discount": 80,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "Hanford Orignal men's brief solo pack white colors",
          "ratings": [13,22,9,5,88],
          "stocks": 2774,
          "reorderlvl": 210,
          "sellingprice": 150,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "George boby athletics supporter brief 10086#",
          "ratings": [8,6,19,79,260],
          "stocks": 564,
          "reorderlvl": 190,
          "sellingprice": 399,
          "discount": 66,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "A&C #1PCS #05 BOXER SHORTS COTTON MENS",
          "ratings": [13,0,27,61,186],
          "stocks": 5805,
          "reorderlvl": 240,
          "sellingprice": 150,
          "discount": 80,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "COD☑️Men's Boxer Underpants Seamless Breathable Middle Waist Underwear Free Size Boxer Briefs",
          "ratings": [16,18,7,45,97],
          "stocks": 2792,
          "reorderlvl": 50,
          "sellingprice": 199,
          "discount": 83,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "6/12PCS MEN'S BRIEF UNDERWEAR FASHION COTTON BRIEFS",
          "ratings": [22,18,12,56,207],
          "stocks": 312,
          "reorderlvl": 150,
          "sellingprice": 268,
          "discount": 53,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "YS 6Pieces Men's 100% Cotton Stripe Boxer Briefs High Quality Underpants",
          "ratings": [17,23,12,64,4],
          "stocks": 1176,
          "reorderlvl": 210,
          "sellingprice": 599,
          "discount": 69,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "YS 6in1 High quality men's boxer brief",
          "ratings": [19,5,30,36,138],
          "stocks": 1894,
          "reorderlvl": 230,
          "sellingprice": 200,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "A&C #6 PCS BH44 STRIPE  BOXER MENS UNDERWEAR COTTON",
          "ratings": [6,4,14,66,157],
          "stocks": 3354,
          "reorderlvl": 240,
          "sellingprice": 750,
          "discount": 72,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "A&C #6 PCS #LAC25 BRIEF MENS UNDERWER COTTON",
          "ratings": [15,2,16,68,94],
          "stocks": 788,
          "reorderlvl": 140,
          "sellingprice": 370,
          "discount": 68,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "12PCS/6PCS Men's Brief Comfortable Wear  COTTON FABRIC",
          "ratings": [16,6,4,13,99],
          "stocks": 1918,
          "reorderlvl": 140,
          "sellingprice": 150,
          "discount": 24,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "Guitar Apparel 1960 M-838 Outside Garter Brief",
          "ratings": [16,16,7,41,72],
          "stocks": 555,
          "reorderlvl": 10,
          "sellingprice": 418,
          "discount": 50,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "R015-330# 6 PCS  100%cotton stretch BRIEF  INSIDE GARTER PLAIN  MENS UNDER WEAR BRIEF .",
          "ratings": [4,21,34,90,209],
          "stocks": 3097,
          "reorderlvl": 100,
          "sellingprice": 400,
          "discount": 60,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "AM 6Pieces Ben*ch body Men's High Quality Cotton Brief New",
          "ratings": [9,18,36,36,261],
          "stocks": 2490,
          "reorderlvl": 100,
          "sellingprice": 799,
          "discount": 79,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "Disposable Brief Men Underwear Non-woven 6 pcs",
          "ratings": [14,1,13,97,2],
          "stocks": 4464,
          "reorderlvl": 120,
          "sellingprice": 30,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "adult cotton boxer short for men",
          "ratings": [4,23,36,38,117],
          "stocks": 1725,
          "reorderlvl": 40,
          "sellingprice": 60,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "BENCH- TUB0311 Men's 3-in-1 Hipster Brief",
          "ratings": [3,15,8,82,42],
          "stocks": 1945,
          "reorderlvl": 110,
          "sellingprice": 40,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "menUnderwear",
          "name": "A&C #1PCS #05 BOXER SHORTS COTTON",
          "ratings": [22,24,43,68,231],
          "stocks": 5317,
          "reorderlvl": 110,
          "sellingprice": 50,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "YS Women Seamless sexy Lingerie Panty underwear panties (free size)",
          "ratings": [16,15,22,71,140],
          "stocks": 1851,
          "reorderlvl": 200,
          "sellingprice": 29.9,
          "discount": 21,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Floral 6/12 PCS. Women's Cotton Underwear Ladies",
          "ratings": [8,16,11,3,39],
          "stocks": 5052,
          "reorderlvl": 180,
          "sellingprice": 999,
          "discount": 91,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "3D Breathable Cotton Hip Soft Stretch Panties Ladies Seamless Lingerie Underwear panty for women",
          "ratings": [16,6,31,8,201],
          "stocks": 5831,
          "reorderlvl": 60,
          "sellingprice": 39,
          "discount": 44,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "12 Colors Ladies Cotton Knickers Underwear Antibacterial Hip Lifting 3D  Slim Panties 610",
          "ratings": [1,4,47,50,90],
          "stocks": 4889,
          "reorderlvl": 180,
          "sellingprice": 102,
          "discount": 75,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Seamless Breathable Premium Silky Soft Sexy Panties Underwear M-2XL Big size 009",
          "ratings": [12,22,33,39,18],
          "stocks": 5372,
          "reorderlvl": 250,
          "sellingprice": 90,
          "discount": 68,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "COOL HOLIDAY High Quality low Waist Slim Panty Body Shaper Warm Palace Honeycomb medium Waist Sexy Hip Briefs high waist belly control body shaping underwear Ladies cotton knickers underwear antibacterial hip lifting 3D cotton Slim panties",
          "ratings": [12,22,6,15,85],
          "stocks": 5792,
          "reorderlvl": 220,
          "sellingprice": 99,
          "discount": 78,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Comfy Seamless High-Quality Ladies Panty Women's Lingerie Girls Panties",
          "ratings": [8,8,31,52,134],
          "stocks": 2030,
          "reorderlvl": 160,
          "sellingprice": 200,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "3D Breathable Cotton Hip Soft Stretch Panties Full Panty Ladies Seamless Lingerie Underwear",
          "ratings": [2,23,3,87,33],
          "stocks": 2725,
          "reorderlvl": 200,
          "sellingprice": 129,
          "discount": 83,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Disposable Panty Women Underwear Non-woven 6 pcs",
          "ratings": [20,22,23,77,299],
          "stocks": 4872,
          "reorderlvl": 30,
          "sellingprice": 109,
          "discount": 0,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Munafie Threaded Women's Triangle Panties Antibacterial Underwear Seamless Cotton with Hip Lifting",
          "ratings": [16,8,4,71,213],
          "stocks": 5493,
          "reorderlvl": 130,
          "sellingprice": 150,
          "discount": 80,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "BESTMOMMY Plus Size M-2XL High Waist Seamless Woman's Shaping Panty Graphene QUALITY GUARANTEE",
          "ratings": [18,0,2,25,38],
          "stocks": 1357,
          "reorderlvl": 10,
          "sellingprice": 299,
          "discount": 86,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "High Quality Breathable High Waist Slimming Girdle Panty Underwear",
          "ratings": [2,3,24,67,221],
          "stocks": 1215,
          "reorderlvl": 140,
          "sellingprice": 98,
          "discount": 60,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "NEW PANTY FOR WOMEN GOOG QUALITY",
          "ratings": [7,0,2,82,174],
          "stocks": 3951,
          "reorderlvl": 60,
          "sellingprice": 189,
          "discount": 48,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "#12 PCS 02-B PANTY PLAIN COTTON SPANDEX GOOD QUALITY COD",
          "ratings": [20,16,42,51,31],
          "stocks": 844,
          "reorderlvl": 140,
          "sellingprice": 220,
          "discount": 27,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Ice seamless panties elastic high quelity women underwear",
          "ratings": [12,8,46,64,228],
          "stocks": 968,
          "reorderlvl": 40,
          "sellingprice": 65,
          "discount": 51,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "CUP SHE Airism Ultra Seamless Shorts（Normal /High Waist/Bikini Three Design to Choose）",
          "ratings": [24,8,5,66,110],
          "stocks": 1470,
          "reorderlvl": 200,
          "sellingprice": 299,
          "discount": 57,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "5XL 7XL Plus Size Stretchable Panties FIT 32 to 44 UP TO 120KG LADIES PANTY WOMEN COTTON UNDERWEAR 1PIECE",
          "ratings": [20,2,22,44,214],
          "stocks": 328,
          "reorderlvl": 240,
          "sellingprice": 100,
          "discount": 71,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "High Quality Warm Palace Honeycomb medium Waist Sexy Hip Briefs high waist belly control body shaping underwear",
          "ratings": [21,21,27,89,148],
          "stocks": 5497,
          "reorderlvl": 100,
          "sellingprice": 119,
          "discount": 81,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "[GALA] High Quality low Waist Slim Panty Body Shaper Warm Palace Honeycomb medium Waist Sexy Hip Briefs high waist belly control body shaping underwear Ladies cotton knickers underwear antibacterial hip lifting 3D cotton Slim panties",
          "ratings": [4,19,23,32,233],
          "stocks": 2867,
          "reorderlvl": 80,
          "sellingprice": 98,
          "discount": 79,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Seamless Panty Ice Silk Mid Waist Bikini Panty Briefs Women Underwear Plus Size Lingerie",
          "ratings": [21,6,41,19,186],
          "stocks": 1108,
          "reorderlvl": 20,
          "sellingprice": 35,
          "discount": 36,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Candy Colors Panties Comfortable and Breathable Cute Women Underwear For Ladies",
          "ratings": [17,20,39,74,2],
          "stocks": 828,
          "reorderlvl": 0,
          "sellingprice": 97,
          "discount": 70,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Women Seamless Keep Abdomen Comfortable Lingerie Panty Underwear cotton Panties 610",
          "ratings": [17,15,21,35,238],
          "stocks": 5429,
          "reorderlvl": 190,
          "sellingprice": 102,
          "discount": 75,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "16 Colors Ice Silk Seamless Underwear PS006",
          "ratings": [17,6,24,26,37],
          "stocks": 5578,
          "reorderlvl": 40,
          "sellingprice": 158,
          "discount": 80,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Women Ice Silk Seamless Panties Panty Invisible Breathable Briefs Underwear Pants",
          "ratings": [17,8,23,15,163],
          "stocks": 5397,
          "reorderlvl": 150,
          "sellingprice": 80,
          "discount": 52,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "High quality Cotton Panty Underwear Elastic Design Women Tummy Control Middle Waist Cotton Panties",
          "ratings": [13,3,0,67,254],
          "stocks": 612,
          "reorderlvl": 200,
          "sellingprice": 113,
          "discount": 48,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Umiwear Pure Cotton women Panties 100% Cotton Fabric Medium Waist Tummy Control Elastic Design Elastic Women's underwear",
          "ratings": [21,15,20,76,285],
          "stocks": 1243,
          "reorderlvl": 220,
          "sellingprice": 149,
          "discount": 70,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Maternity Underwear Women Pregnant Panties Cotton U-Shaped Low Waist Panty",
          "ratings": [9,21,35,99,236],
          "stocks": 5711,
          "reorderlvl": 0,
          "sellingprice": 100,
          "discount": 42,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Timi 700 High quality 1 Pcs Ice-silk briefs seamless Underpants Women Underwears Mid-rise panty",
          "ratings": [1,9,21,55,236],
          "stocks": 3040,
          "reorderlvl": 80,
          "sellingprice": 95,
          "discount": 59,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "MUNAFIE Women's Seamless Butt Lifter Seamless Panties Munafie Panties panty",
          "ratings": [22,18,31,66,246],
          "stocks": 313,
          "reorderlvl": 70,
          "sellingprice": 69,
          "discount": 58,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "V.S High Quality Lingerie Panty for Women (1PC) Free Size, Random Color #148",
          "ratings": [9,5,50,27,129],
          "stocks": 4469,
          "reorderlvl": 200,
          "sellingprice": 99,
          "discount": 49,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Women Seamless Cotton sexy Lingerie Panty underwear Thread lace trim panties C11",
          "ratings": [15,4,44,29,65],
          "stocks": 2038,
          "reorderlvl": 110,
          "sellingprice": 80,
          "discount": 61,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Plain Panty Cotton Underwear Women seamless Panties B03",
          "ratings": [10,16,33,57,241],
          "stocks": 4902,
          "reorderlvl": 170,
          "sellingprice": 80,
          "discount": 73,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Umiwear Seamless Breathable Ultra Thin Silky Soft Sexy Panties High Quality Ice-silk Ladies Seamless Panty",
          "ratings": [23,4,38,50,101],
          "stocks": 5205,
          "reorderlvl": 220,
          "sellingprice": 99,
          "discount": 71,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Women Ice silk seamless mid-rise sexy panty triangle briefs for ladies panties",
          "ratings": [17,9,3,35,12],
          "stocks": 2119,
          "reorderlvl": 130,
          "sellingprice": 150,
          "discount": 81,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Women's High Quality Breathable High Waist Slimming Girdle Panty Underwear Panties Brief",
          "ratings": [21,15,8,90,218],
          "stocks": 5412,
          "reorderlvl": 100,
          "sellingprice": 150,
          "discount": 77,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Plus size M-XL High Waist Moulding Breathable Munafie Panty",
          "ratings": [9,14,19,68,168],
          "stocks": 979,
          "reorderlvl": 130,
          "sellingprice": 100,
          "discount": 57,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "10 Colors Seamless Oxygen Bubble Underwear Breathable Lace Mid Waist Girl Sexy Lady 's Briefs 1791",
          "ratings": [14,1,36,3,189],
          "stocks": 4809,
          "reorderlvl": 210,
          "sellingprice": 80,
          "discount": 61,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "CAYO High Waist Belly Control Body Shaping Girdle Underwear Antibacterial Hip Lifting Belly Control Cotton Panties",
          "ratings": [16,4,46,3,109],
          "stocks": 2658,
          "reorderlvl": 230,
          "sellingprice": 120,
          "discount": 68,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "Munafie Threaded Women's Triangle Panties Antibacterial Underwear Seamless Cotton with Hip Lifting",
          "ratings": [4,2,43,60,36],
          "stocks": 3416,
          "reorderlvl": 180,
          "sellingprice": 299,
          "discount": 89,
          "isarchived": 0
        },
        {
          "category": "womenUnderwear",
          "name": "12 Colors Women tall waist non-trace panty Munafie-Girdle Lingerie 328",
          "ratings": [19,5,45,4,123],
          "stocks": 742,
          "reorderlvl": 120,
          "sellingprice": 169,
          "discount": 78,
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