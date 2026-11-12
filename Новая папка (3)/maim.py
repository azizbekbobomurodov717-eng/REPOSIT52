import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

TOKEN = "8752993009:AAFhWJjbT-O5cZ9x5UIlmoajc-iYUVtnlXs"

bot = Bot(token=TOKEN)
dp = Dispatcher()

REGIONS_DATA = {
    "navoiy": {
        "title": "Navoiy viloyati",
        "photo": "https://migrationunion.com/wp-content/uploads/2024/06/navoiy.jpg",
        "info": "Navoiy viloyati — yirik sanoat va konchilik markazi.",
        "districts": {
            "Karmana": {"photo": "https://uzbek-travel.com/images/uz/Landmarks/Navoi/Kamrana/11119513103_fa8d72920c_o.jpg", "info": "📍 Karmana tumani — qadimiy tarixga ega tuman."},
            "Navbahor": {"photo": "https://cdn.uza.uz/2020/10/02/11/24/OYp3Kh9nuuacrRSMP1H7RMI79iLsJ0hi_normal.jpg", "info": "📍 Navbahor tumani — qishloq xo'jaligiga ixtisoslashgan."},
            "Qiziltepa": {"photo": "https://yandex-images.clstorage.net/47qRQo236/0b6bc4sgfp/HF5ULqv891CdsR-vIyHXHHgM-QMed-205N07wQDXAe1hu0cXSdDHABZCJzvz_cgPmGMjz2pH3AZKF4qPzuwQrwgeWDLg-7kH3udc7TR7gQpgQKtCIkrZxeLdJokPxiqfQZZxKX-tv3NsP2hor6CCRdcmaaAFV4JtIwDd3Iy_PsUOTCR7xdvUYYGIBp5DBMsLMTHIHj9W--Pw1xmIMv8MhVe7WTRSlpx5YSd1cLi-ikSPMUGMKBOlWTUg0Parvgf2AH8jY-DSxUKzkh6pXwL1ByUv2yQcZf3V8M06mz7dL655tGI-ZIaCYmc1WGWTrK5vnBhYljkirH00NPrNqLIr8jlZFmPR9u1ko7Y_uWIa0DsSEPIVFGfT7-D3C50B1x-QY55RFEi5olh0K3xGrIyNUao2V4gJEqZaMzrq846iFM4oQgpu5tzVULGRIbBIK8kGFTfuOzhX18zz_yabK-IYjlOdeSdRs59QUxN6b6uCpFSaG3-FNS-oZz82xu6wjTXQH2g3YMfP91-7txSrfiHyHiUi1i44U_j54cArvyHoE5V2jloVSbSjXkwbRGaqsZVUvQB-sjAVlW0IIfbdq54V1w5PLETX7Ph6uZgKmlwZ2g4iBskUHmft8ebOJIAd-RKtUaNcFEi9pW5iMnxOoK2VZaMCRI4gIYhLJSvJ76izJM8gSTtL3s7Uaaq7ALR4JuAdODPxIQt2-tPt4T2rH-Mwt3SVdR1Vh5pZZBd5Q4uDnlCOHle6CBSOUCoy8saWrTHrDmQbVcncxESuoSe0aAvmLhMf8zkIfOPL-fsnoyvLFrV4lVQZWp2ERH8CXkuzq41NlhZ6qikHhXYeJMTdkpQZ2iFIP03OxO50voI8s0g_3j0aAOgiHVbE3sngDr8K3zmsTrRSOHempHFXP3R6tLyyapwkUrAgBbxWOgbT0KKjMOQjRwpn4fv2e6GiNaR6NPksGCPtDx5h_uP86QuKKuQ", "info": "📍 Qiziltepa tumani — viloyatning yirik tumanlaridan."},
            "Nurota": {"photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Nurota_mosque_and_source.JPG/960px-Nurota_mosque_and_source.JPG", "info": "📍 Nurota tumani — ziyorat turizmi va buloqlari bilan mashhur."},
            "Xatirchi": {"photo": "https://agroturizm.uz/images/Xatirchi0.png", "info": "📍 Xatirchi tumani — qadimiy dehqonchilik maskani."},
            "Uchquduq": {"photo": "https://yuz.uz/imageproxy/980x/https://yuz.uz/file/news/b647219d1d2d8e7235a353adef306c1b.jpg", "info": "🏙 Uchquduq shahri — quduqlar va sanoat shahri."},
            "Tamdi": {"photo": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Tamdy_District%2C_Uzbekistan_-_panoramio_%28124%29.jpg", "info": "📍 Tomdi tumani — cho'l hududida joylashgan tuman."},
            "Kanimex": {"photo": "https://i.ytimg.com/vi/_7YpKeVjoRM/maxresdefault.jpg", "info": "📍 Konimex tumani — chorvachilikka boy hudud."},
            "Zarafshon": {"photo": "https://arxiv.uz/data/documents/d5ce8184-b00b-4418-ab76-9940b916fd82/page-1.lcp.webp", "info": "🏙 Zarafshon shahri — cho'l bag'ridagi oltin shahri."}
        }
    },
    "buxoro": {
        "title": "Buxoro viloyati",
        "photo": "https://resize.tripster.ru/bg7ee3iplSC7qRz4vQjjskMfzoQ=/fit-in/1080x810/filters:no_upscale()/https://cdn.tripster.ru/photos/80fd7e76-b7a9-4735-b91d-a6740d055ef2.jpg",
        "info": "Buxoro viloyati — qadimiy tarix va jahon turizmi markazi.",
        "districts": {
            "G'ijduvon": {"photo": "https://www.turkestantravel.com/wp-content/uploads/2020/12/Ulugbek-Medrese-Gidschduwan.jpg", "info": "📍 G'ijduvon tumani — kulolchilik va shashlik markazi."},
            "Kogon": {"photo": "https://pastvu.com/_p/a/e/t/f/etfnaot3t09kmpsx15.jpg", "info": "🏙 Kogon shahri va tumani — muhim temir yo'l tuguni."},
            "Vobkent": {"photo": "https://dkm.gov.uz/uploads/2020/08/vgolpgnldangdanoryvkepivkeprekr.jpg", "info": "📍 Vobkent tumani — qadimiy minorasi bilan mashhur."},
            "Jondor": {"photo": "https://i.ytimg.com/vi/-_eSAzimtGw/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgWChPMA8=&amp;rs=AOn4CLDR0A1tdpiYs_RZytrRGzqBWbBydw", "info": "📍 Jondor tumani — dehqonchilik hududi."},
            "Olot": {"photo": "https://i.ytimg.com/vi/CMdRQreW3Vk/maxresdefault.jpg", "info": "📍 Olot tumani — viloyatning janubiy tumanlaridan."},
            "Romitan": {"photo": "https://avatars.mds.yandex.net/get-altay/12820607/2a000001926f4dd2e45e0bfa91c20b6fa84a/XXL_height", "info": "📍 Romitan tumani — qadimiy qadamjolar maskani."},
            "Qorako'l": {"photo": "https://cdn.uza.uz/2023/07/14/09/22/4IzPRrZlGK1eOuVpUDYh37e2dBVTtASp_front.jpg", "info": "📍 Qorako'l tumani — ta'lim va qorako'lchilik markazi."},
            "Peshku": {"photo": "https://teznews.uz/wp-content/uploads/2020/09/b5ffad1415c2e56116806-e1599026904720.jpg", "info": "📍 Peshku tumani — yirik hududlardan biri."},
            "Shofirkon": {"photo": "https://avatars.mds.yandex.net/get-altay/11203687/2a000001927131c9dd1ea32c8b167c08e8a9/XXL_height", "info": "📍 Shofirkon tumani — tarixiy obidalarga boy."}
        }
    },
    "samarqand": {
        "title": "Samarqand viloyati",
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/RegistanSquare_Samarkand.jpg/1280px-RegistanSquare_Samarkand.jpg",
        "info": "Samarqand — Sharq gavhari va dunyoning qadimiy shahri.",
        "districts": {
            "Urgut": {"photo": "https://turkic.world/media/2024/01/16/urgut.jpg", "info": "📍 Urgut tumani — go'zal tabiati va yirik bozori bilan mashhur."},
            "Kattaqo'rg'on": {"photo": "https://picsum.photos/seed/kattaqorgon/600/300", "info": "🏙 Kattaqo'rg'on shahri va tumani — suv ombori va tarix."},
            "Jomboy": {"photo": "https://picsum.photos/seed/jomboy/600/300", "info": "📍 Jomboy tumani — dehqonchilik va bog'dorchilik."},
            "Pastdarg'om": {"photo": "https://picsum.photos/seed/pastdargom/600/300", "info": "📍 Pastdarg'om tumani — aholisi ko'p tumanlardan."},
            "Ishtixon": {"photo": "https://picsum.photos/seed/ishtixon/600/300", "info": "📍 Ishtixon tumani — qadimiy Shahri Islom yodgorligi."},
            "Payariq": {"photo": "https://picsum.photos/seed/payariq/600/300", "info": "📍 Payariq tumani — Imom Buxoriy ziyoratgohi joylashgan."},
            "Bulung'ur": {"photo": "https://picsum.photos/seed/bulungur/600/300", "info": "📍 Bulung'ur tumani — meva-sabzavot yetishtirishga boy."},
            "Narpay": {"photo": "https://picsum.photos/seed/narpay/600/300", "info": "📍 Narpay tumani — Zarafshon daryosi bo'yida joylashgan."},
            "Qo'shrabot": {"photo": "https://picsum.photos/seed/qushrabot/600/300", "info": "📍 Qo'shrabot tumani — tog'li va lalmikor hudud."},
            "Tayloq": {"photo": "https://picsum.photos/seed/tayloq/600/300", "info": "📍 Toyloq tumani — Samarqand shahriga yaqin hudud."},
            "Naxshab/Oqdaryo": {"photo": "https://picsum.photos/seed/oqdaryo/600/300", "info": "📍 Oqdaryo tumani — daryo bo'yidagi qishloq xo'jalik tumani."}
        }
    },
    "toshkent": {
        "title": "Toshkent viloyati",
        "photo": "https://cdn1.img.sputniknews.uz/img/07ea/01/15/55124099_0:49:1135:687_2072x0_60_0_0_d270141a243cb60da1bcb49692c93142.jpg",
        "info": "Toshkent viloyati — go'zal tabiat va yirik sanoat hududi.",
        "districts": {
            "Chirchiq": {"photo": "https://avatars.mds.yandex.net/get-altay/13757584/2a00000192ebd6a93016c3ddddedac6679c3/XXL_height", "info": "🏙 Chirchiq shahri — kimyo va mashinasozlik markazi."},
            "Olmaliq": {"photo": "https://picsum.photos/seed/olmaliq/600/300", "info": "🏙 Olmaliq shahri — kon-metallurgiya sanoati markazi."},
            "Angren": {"photo": "https://picsum.photos/seed/angren/600/300", "info": "🏙 Angren shahri — ko'mir sanoati va energetika shahri."},
            "Bekobod": {"photo": "https://picsum.photos/seed/bekobod/600/300", "info": "🏙 Bekobod shahri — metallurglar shahri (O'zmetkombinat)."},
            "Yangiyo'l": {"photo": "https://picsum.photos/seed/yangiyol/600/300", "info": "🏙 Yangiyo'l shahri va tumani — qishloq xo'jaligi markazi."},
            "Bo'ka": {"photo": "https://picsum.photos/seed/boka/600/300", "info": "📍 Bo'ka tumani — dehqonchilikka ixtisoslashgan."},
            "Zangiota": {"photo": "https://picsum.photos/seed/zangiota/600/300", "info": "📍 Zangiota tumani — muqaddas Zangiota ziyoratgohi."},
            "Qibray": {"photo": "https://picsum.photos/seed/qibray/600/300", "info": "📍 Qibray tumani — bog'lar va ilmiy markazlar hududi."},
            "Parkent": {"photo": "https://picsum.photos/seed/parkent/600/300", "info": "📍 Parkent tumani — Quyosh instituti va uzumlari bilan mashhur."},
            "Bo'stonliq": {"photo": "https://picsum.photos/seed/bostonliq/600/300", "info": "📍 Bo'stonliq tumani — Chorvoq va Chimyon tog' dam olish maskani."},
            "Yuqori Chirchiq": {"photo": "https://picsum.photos/seed/yuqorichirchiq/600/300", "info": "📍 Yuqori Chirchiq tumani — Toshkent atrofi hududi."},
            "O'rta Chirchiq": {"photo": "https://picsum.photos/seed/ortachirchiq/600/300", "info": "📍 O'rta Chirchiq tumani — To'ytepa shahri markazi."},
            "Quyi Chirchiq": {"photo": "https://picsum.photos/seed/quyichirchiq/600/300", "info": "📍 Quyi Chirchiq tumani — dehqonchilik tumani."},
            "Chinoz": {"photo": "https://picsum.photos/seed/chinoz/600/300", "info": "📍 Chinoz tumani — baliqchilik va daryo bo'yi hududi."},
            "Piskent": {"photo": "https://picsum.photos/seed/piskent/600/300", "info": "📍 Piskent tumani — qadimiy hunarmandchilik maskani."},
            "Toshkent tumani": {"photo": "https://picsum.photos/seed/toshkenttumani/600/300", "info": "📍 Toshkent tumani — poytaxt yaqinidagi tuman."}
        }
    },
    "fargona": {
        "title": "Farg'ona viloyati",
        "photo": "https://irecommend.ru/sites/default/files/product-images/2870754/3RwfHeTb69MaG5aFaoFvQ.jpg",
        "info": "Farg'ona viloyati — vodiyning yirik sanoat va bog'dorchilik markazi.",
        "districts": {
            "Marg'ilon": {"photo": "https://avatars.mds.yandex.net/get-altay/15696528/2a0000019e106df58b168ab4bb266bf8297d/XXL_height", "info": "🏙 Marg'ilon shahri — asrlar osha ipak va adras markazi."},
            "Qo'qon": {"photo": "https://picsum.photos/seed/qoqon/600/300", "info": "🏙 Qo'qon shahri — Qo'qon xonligi poytaxti, tarixiy shahar."},
            "Quvasoy": {"photo": "https://picsum.photos/seed/quvasoy/600/300", "info": "🏙 Quvasoy shahri — sement va sanoat shahri."},
            "Rishton": {"photo": "https://picsum.photos/seed/rishton/600/300", "info": "📍 Rishton tumani — Markaziy Osiyodagi sirli kulolchilik markazi."},
            "Oltiariq": {"photo": "https://picsum.photos/seed/oltiariq/600/300", "info": "📍 Oltiariq tumani — shirin uzumlari bilan mashhur."},
            "Quva": {"photo": "https://picsum.photos/seed/quva/600/300", "info": "📍 Quva tumani — qadimiy arxeologik topilmalar maskani."},
            "Beshariq": {"photo": "https://picsum.photos/seed/beshariq/600/300", "info": "📍 Beshariq tumani — viloyatning g'arbiy darvozasi."},
            "Uchko'prik": {"photo": "https://picsum.photos/seed/uchkoprik/600/300", "info": "📍 Uchko'prik tumani — qishloq xo'jaligi rivojlangan."},
            "Dang'ara": {"photo": "https://picsum.photos/seed/dangara/600/300", "info": "📍 Dang'ara tumani — savdo va dehqonchilik."},
            "Furqat": {"photo": "https://picsum.photos/seed/furqat/600/300", "info": "📍 Furqat tumani — shoir nomi berilgan hudud."},
            "Bag'dod": {"photo": "https://picsum.photos/seed/bagdod/600/300", "info": "📍 Bag'dod tumani — yirik tumanlardan biri."},
            "Buvayda": {"photo": "https://picsum.photos/seed/buvayda/600/300", "info": "📍 Buvayda tumani — ziyoratgoh va qadimiy qishloqlar."},
            "Yozyovon": {"photo": "https://picsum.photos/seed/yozyovon/600/300", "info": "📍 Yozyovon tumani — cho'l hududida o'zlashtirilgan yerlar."},
            "Toshloq": {"photo": "https://picsum.photos/seed/toshloq/600/300", "info": "📍 Toshloq tumani — bog'dorchilik va hunarmandchilik."}
        }
    },
    "namangan": {
        "title": "Namangan viloyati",
        "photo": "https://cdn.uza.uz/2026/08/19/12/20/EJSPST7TrvpwZ2XljnqpMAuHuhOmhXPD_normal.jpg",
        "info": "Namangan viloyati — gullar shahri va to'qimachilik markazi.",
        "districts": {
            "Chust": {"photo": "https://i.ytimg.com/vi/bKrTlcXfCFA/maxresdefault.jpg", "info": "📍 Chust tumani — milliy pichoqlar va do'ppiduzlik maskani."},
            "Kosonsoy": {"photo": "https://picsum.photos/seed/kosonsoy/600/300", "info": "📍 Kosonsoy tumani — qadimiy va sersuv tabiatli tuman."},
            "Chortoq": {"photo": "https://picsum.photos/seed/chortoq/600/300", "info": "📍 Chortoq tumani — shifobaxsh mineral suvlari va sanatoriylari bor."},
            "Uychi": {"photo": "https://picsum.photos/seed/uychi/600/300", "info": "📍 Uychi tumani — Sirdaryo bo'yidagi qishloq xo'jalik tumani."},
            "To'raqo'rg'on": {"photo": "https://picsum.photos/seed/toraqorgon/600/300", "info": "📍 To'raqo'rg'on tumani — Ishoqxon Ibrat majmuasi joylashgan."},
            "Pop": {"photo": "https://picsum.photos/seed/pop/600/300", "info": "📍 Pop tumani — hududi jihatidan eng yirik tumanlardan biri."},
            "Mingbuloq": {"photo": "https://picsum.photos/seed/mingbuloq/600/300", "info": "📍 Mingbuloq tumani — neft quduqlari va dehqonchilik."},
            "Yangiqo'rg'on": {"photo": "https://picsum.photos/seed/yangiqorgon/600/300", "info": "📍 Yangiqo'rg'on tumani — tog'oldi hududi va dam olish maskanlari."},
            "Norin": {"photo": "https://picsum.photos/seed/norin/600/300", "info": "📍 Norin tumani — milliy osh va daryo bo'yi hududi."},
            "Uchqo'rg'on": {"photo": "https://picsum.photos/seed/uchqorgon/600/300", "info": "📍 Uchqo'rg'on tumani — GES va sanoat korxonalari joylashgan."}
        }
    },
    "andijon": {
        "title": "Andijon viloyati",
        "photo": "https://people-travels.com/storage/manager/Andijansights/Andijan-city.jpg",
        "info": "Andijon viloyati — zich aholili va mashinasozlik markazi.",
        "districts": {
            "Asaka": {"photo": "https://storage.kun.uz/source/4/V-bI9G4zjKCrQtLyI7M-rFrf7M9uNhLW.jpg", "info": "🏙 Asaka shahri va tumani — O'zbekiston avtomobilsozlik zavodi joylashgan."},
            "Shahrixon": {"photo": "https://picsum.photos/seed/shahrixon/600/300", "info": "📍 Shahrixon tumani — pichoqchilik va savdo-sotiq markazi."},
            "Xonobod": {"photo": "https://picsum.photos/seed/xonobod/600/300", "info": "🏙 Xonobod shahri — vodiyning Shveytsariyasi deb nomlanuvchi kurort shahar."},
            "Xo'jaobod": {"photo": "https://picsum.photos/seed/xojaobod/600/300", "info": "📍 Xo'jaobod tumani — mebelsozlik va hunarmandchilik."},
            "Jalaquduq": {"photo": "https://picsum.photos/seed/jalaquduq/600/300", "info": "📍 Jalaquduq tumani — qishloq xo'jaligi rivojlangan."},
            "Marhamat": {"photo": "https://picsum.photos/seed/marhamat/600/300", "info": "📍 Marhamat tumani — qadimiy Mingtepa shahri harobasi joylashgan."},
            "Izboskan": {"photo": "https://picsum.photos/seed/izboskan/600/300", "info": "📍 Izboskan tumani — yirik aholi punktlaridan biri."},
            "Paxtaobod": {"photo": "https://picsum.photos/seed/paxtaobod/600/300", "info": "📍 Paxtaobod tumani — dehqonchilik va paxtachilik."},
            "Buloqboshi": {"photo": "https://picsum.photos/seed/buloqboshi/600/300", "info": "📍 Buloqboshi tumani — milliy hunarmandchilik va beshikchilik."},
            "Qo'rg'ontepa": {"photo": "https://picsum.photos/seed/qorgontepa/600/300", "info": "📍 Qo'rg'ontepa tumani — chegaraoldi tuman."},
            "Ulug'nor": {"photo": "https://picsum.photos/seed/ulugnor/600/300", "info": "📍 Ulug'nor tumani — cho'l hududini o'zlashtirish natijasida tashkil topgan."},
            "Oltinko'l": {"photo": "https://picsum.photos/seed/oltinkol/600/300", "info": "📍 Oltinko'l tumani — sabzavotchilikka ixtisoslashgan."},
            "Baliqchi": {"photo": "https://picsum.photos/seed/baliqchi/600/300", "info": "📍 Baliqchi tumani — daryo bo'yida joylashgan."}
        }
    },
    "jizzax": {
        "title": "Jizzax viloyati",
        "photo": "https://central-asia.guide/wp-content/uploads/2021/01/Jizzakh_square.jpg",
        "info": "Jizzax viloyati — go'zal tabiat va Zomin tog'lari maskani.",
        "districts": {
            "Zomin": {"photo": "https://eurasia.travel/wp-content/uploads/2024/07/Zaamin-sanatorium-4.jpg", "info": "📍 Zomin tumani — O'zbek Shveytsariyasi, archazor tog'lar."},
            "G'allaorol": {"photo": "https://picsum.photos/seed/gallaorol/600/300", "info": "📍 G'allaorol tumani — g'alla va lalmikor dehqonchilik."},
            "Paxtakor": {"photo": "https://picsum.photos/seed/paxtakor/600/300", "info": "📍 Paxtakor tumani — fermerlik va paxtachilik."},
            "Forish": {"photo": "https://picsum.photos/seed/forish/600/300", "info": "📍 Forish tumani — hududi bo'yicha eng katta tumanlardan, Aydarko'l."},
            "Arnasoy": {"photo": "https://picsum.photos/seed/arnasoy/600/300", "info": "📍 Arnasoy tumani — ko'llar va baliqchilik maskani."},
            "Do'stlik": {"photo": "https://picsum.photos/seed/dostlik/600/300", "info": "📍 Do'stlik tumani — shaharcha tipidagi tuman."},
            "Mirzacho'l": {"photo": "https://picsum.photos/seed/mirzachol/600/300", "info": "📍 Mirzacho'l tumani (Gagarin shahri) — cho'l o'zlashtirish markazi."},
            "Zafarobod": {"photo": "https://picsum.photos/seed/zafarobod/600/300", "info": "📍 Zafarobod tumani — sanoat va qishloq xo'jaligi."},
            "Sharof Rashidov": {"photo": "https://picsum.photos/seed/sharofrashidov/600/300", "info": "📍 Sharof Rashidov tumani — viloyat markazi atrofidagi yirik tuman"},
            "Baxmal": {"photo": "https://picsum.photos/seed/baxmal/600/300", "info": "📍 Baxmal tumani — olmalari va tog'li tabiati bilan mashhur."}
        }
    },
    "qashqadaryo": {
        "title": "Qashqadaryo viloyati",
        "photo": "https://avatars.mds.yandex.net/i?id=d5a2fa8d60d2dd4512a5b8042235cf050b385c4d-3948701-images-thumbs&n=13",
        "info": "Qashqadaryo viloyati — neft-gaz sanoati va tarixiy meros.",
        "districts": {
            "Qarshi sh.": {"photo": "https://picsum.photos/seed/qarshish/600/300", "info": "🏙 Qarshi shahri — qadimiy Nasaf, viloyat markazi."},
            "Shahrisabz": {"photo": "https://picsum.photos/seed/shahrisabz/600/300", "info": "🏙 Shahrisabz shahri — Amir Temur vatani, Oqsaroy maskani."},
            "Kitob": {"photo": "https://picsum.photos/seed/kitob/600/300", "info": "📍 Kitob tumani — geofizika stansiyasi va tog'li hudud."},
            "G'uzor": {"photo": "https://picsum.photos/seed/guzor/600/300", "info": "📍 G'uzor tumani — neft-gaz sanoati korxonalari joylashgan."},
            "Chiroqchi": {"photo": "https://picsum.photos/seed/chiroqchi/600/300", "info": "📍 Chiroqchi tumani — aholisi ko'p yirik tuman."},
            "Yakkabog'": {"photo": "https://picsum.photos/seed/yakkabog/600/300", "info": "📍 Yakkabog' tumani — tog'oldi dehqonchilik hududi."},
            "Qamashi": {"photo": "https://picsum.photos/seed/qamashi/600/300", "info": "📍 Qamashi tumani — tabiri va daryolari bor tuman."},
            "Kasbi": {"photo": "https://picsum.photos/seed/kasbi/600/300", "info": "📍 Kasbi tumani — qishloq xo'jaligiga ixtisoslashgan."},
            "Mirishkor": {"photo": "https://picsum.photos/seed/mirishkor/600/300", "info": "📍 Mirishkor tumani — chorvachilik va dehqonchilik."},
            "Nishon": {"photo": "https://picsum.photos/seed/nishon/600/300", "info": "📍 Nishon tumani — Talimarjon GES va energetika markazi."},
            "Dehqonobod": {"photo": "https://picsum.photos/seed/dehqonobod/600/300", "info": "📍 Dehqonobod tumani — kaliy tuzlari koni va tog'lar."},
            "Koson": {"photo": "https://picsum.photos/seed/koson/600/300", "info": "📍 Koson tumani — qadimiy Estarkon shahri o'rni."}
        }
    },
    "surxandaryo": {
        "title": "Surxandaryo",
        "photo": "https://cdn.uza.uz/2024/01/24/05/18/QE8BnUcQNuSCZlW9qW9aXlAkRRJvEMEI_normal.jpg",
        "info": "Surxandaryo viloyati — eng janubiy, quyoshli va qadimiy o'lka.",
        "districts": {
            "Termiz sh.": {"photo": "https://eurasia.travel/wp-content/uploads/2024/07/termez-2.jpg", "info": "🏙 Termiz shahri — ming yillik buddizm va islom sivilizatsiyasi markazi."},
            "Denov": {"photo": "https://picsum.photos/seed/denov/600/300", "info": "🏙 Denov shahri va tumani — viloyatning yirik savdo va bog'dorchilik markazi."},
            "Sherobod": {"photo": "https://picsum.photos/seed/sherobod/600/300", "info": "📍 Sherobod tumani — mashhur Sherobod qovunlari vatani."},
            "Boysun": {"photo": "https://picsum.photos/seed/boysun/600/300", "info": "📍 Boysun tumani — YuNESKO madaniy merosiga kirgan qadimiy maskan."},
            "Sariosiyo": {"photo": "https://picsum.photos/seed/sariosiyo/600/300", "info": "📍 Sariosiyo tumani — Xonto'g'ay sharsharasi va tog'lar."},
            "Uzun": {"photo": "https://picsum.photos/seed/uzun/600/300", "info": "📍 Uzun tumani — eng chekka shimoliy tumanlardan."},
            "Jarqo'rg'on": {"photo": "https://picsum.photos/seed/jarqorgon/600/300", "info": "📍 Jarqo'rg'on tumani — noyob Jarqo'rg'on minorasi joylashgan."},
            "Qumqo'rg'on": {"photo": "https://picsum.photos/seed/qumqorgon/600/300", "info": "📍 Qumqo'rg'on tumani — temir yo'l kesishmasi va dehqonchilik."},
            "Angor": {"photo": "https://picsum.photos/seed/angor/600/300", "info": "📍 Angor tumani — paxtachilik va sabzavotchilik."},
            "Muzrabot": {"photo": "https://picsum.photos/seed/muzrabot/600/300", "info": "📍 Muzrabot tumani — chegaraoldi qishloq xo'jalik tumani."},
            "Bandixon": {"photo": "https://picsum.photos/seed/bandixon/600/300", "info": "📍 Bandixon tumani — yangi tashkil etilgan tumanlardan."},
            "Qiziriq": {"photo": "https://picsum.photos/seed/qiziriq/600/300", "info": "📍 Qiziriq tumani — dehqonchilik va bog'lar."}
        }
    },
    "sirdaryo": {
        "title": "Sirdaryo viloyati",
        "photo": "https://cdn.uza.uz/2022/08/30/10/42/qMEEYPcb5hF4zVe0pzJTM0FSZjPp248E_normal.JPG",
        "info": "Sirdaryo viloyati — paxta, g'alla va daryo bo'yi o'lkasi.",
        "districts": {
            "Guliston sh.": {"photo": "https://avatars.mds.yandex.net/i?id=340330e98befbe3ce3697e77814197c30b47df5f-5206685-images-thumbs&n=13", "info": "🏙 Guliston shahri — Sirdaryo viloyatining ma'muriy markazi."},
            "Yangiyer": {"photo": "https://picsum.photos/seed/yangiyer/600/300", "info": "🏙 Yangiyer shahri — sanoat va ta'lim maskani."},
            "Shirin": {"photo": "https://picsum.photos/seed/shirin/600/300", "info": "🏙 Shirin shahri — Sirdaryo GES energetiklari shahri."},
            "Sirdaryo tumani": {"photo": "https://picsum.photos/seed/sirdaryotumani/600/300", "info": "📍 Sirdaryo tumani — daryo bo'yidagi qishloq xo'jalik hududi."},
            "Boyovut": {"photo": "https://picsum.photos/seed/boyovut/600/300", "info": "📍 Boyovut tumani — dehqonchilik va fermerlik."},
            "Sayxunobod": {"photo": "https://picsum.photos/seed/sayxunobod/600/300", "info": "📍 Sayxunobod tumani — bog'dorchilik va sabzavotchilik."},
            "Oqoltin": {"photo": "https://picsum.photos/seed/oqoltin/600/300", "info": "📍 Oqoltin tumani — paxtachilik va g'allachilik."},
            "Sardoba": {"photo": "https://picsum.photos/seed/sardoba/600/300", "info": "📍 Sardoba tumani — tarixiy sardoba inshooti va qishloq xo'jaligi."},
            "Mirzaobod": {"photo": "https://picsum.photos/seed/mirzaobod/600/300", "info": "📍 Mirzaobod tumani — Toshkent yo'lidagi yirik tuman."}
        }
    },
    "xorazm": {
        "title": "Xorazm viloyati",
        "photo": "https://avatars.mds.yandex.net/i?id=75cb82a569d83d62e5cdd9897e4b08526bc6b035-4843806-images-thumbs&n=13",
        "info": "Xorazm viloyati — qadimiy davlatchilik va Ichan-qal'a maskani.",
        "districts": {
            "Urganch sh.": {"photo": "https://content.centrum-air.com/media/news_images/7c63df58-fd5d-45d8-be00-3abd8de630dd.jpg", "info": "🏙 Urganch shahri — Xorazm viloyatining zamonaviy markazi."},
            "Xiva": {"photo": "https://picsum.photos/seed/xiva/600/300", "info": "🏙 Xiva shahri — ochiq osmon ostidagi muzey, Ichan-qal'a."},
            "Xonqa": {"photo": "https://picsum.photos/seed/xonqa/600/300", "info": "📍 Xonqa tumani — hunarmandchilik va dehqonchilik."},
            "Shovot": {"photo": "https://picsum.photos/seed/shovot/600/300", "info": "📍 Shovot tumani — kanal bo'yidagi yirik tuman."},
            "Gurlan": {"photo": "https://picsum.photos/seed/gurlan/600/300", "info": "📍 G'urlan tumani — dehqonchilik va qadimiy tarix."},
            "Yangiariq": {"photo": "https://picsum.photos/seed/yangiariq/600/300", "info": "📍 Yangiariq tumani — bog'lar va qishloq xo'jaligi."},
            "Yangibozor": {"photo": "https://picsum.photos/seed/yangibozor/600/300", "info": "📍 Yangibozor tumani — savdo va dehqonchilik."},
            "Hazorasp": {"photo": "https://picsum.photos/seed/hazorasp/600/300", "info": "📍 Hazorasp tumani — qadimiy qal'a va tarixiy hudud."},
            "Bog'ot": {"photo": "https://picsum.photos/seed/bogot/600/300", "info": "📍 Bog'ot tumani — poliz ekinlari va dehqonchilik."},
            "Qo'shko'pir": {"photo": "https://picsum.photos/seed/qoshkopir/600/300", "info": "📍 Qo'shko'pir tumani — zich aholili tumanlardan biri."}
        }
    }
}


    
def get_regions_keyboard():
    regions = list(REGIONS_DATA.keys())
    keyboard = []
    
    for i in range(0, len(regions), 3):
        row = []
        for j in range(3):
            if i + j < len(regions):
                r_key = regions[i + j]
                row.append(InlineKeyboardButton(text=REGIONS_DATA[r_key]["title"].split()[0], callback_data=f"vil_{r_key}"))
        keyboard.append(row)
        
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_districts_keyboard(region_key: str):
    if region_key not in REGIONS_DATA or "districts" not in REGIONS_DATA[region_key]:
        return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ Bosh menyuga qaytish", callback_data="back_to_main")]])
        
    districts = REGIONS_DATA[region_key]["districts"]
    keyboard = []
    district_keys = list(districts.keys())
    
    for i in range(0, len(district_keys), 2):
        row = [InlineKeyboardButton(text=district_keys[i], callback_data=f"tum_{region_key}_{district_keys[i]}")]
        if i + 1 < len(district_keys):
            row.append(InlineKeyboardButton(text=district_keys[i+1], callback_data=f"tum_{region_key}_{district_keys[i+1]}"))
        keyboard.append(row)
    
    keyboard.append([InlineKeyboardButton(text="⬅️ Bosh menyuga qaytish", callback_data="back_to_main")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)



@dp.message(CommandStart())
async def start_handler(message: Message):
    main_photo = "https://picsum.photos/seed/uzbekistan/600/400"
    
    await message.answer_photo(
        photo=main_photo,
        caption="🇺🇿 **Salom, botimizga xush kelibsiz!**\n\nIltimos, kerakli viloyatni tanlang:",
        reply_markup=get_regions_keyboard()
    )

@dp.callback_query(F.data.startswith("vil_"))
async def region_selected(callback: CallbackQuery):
    region_key = callback.data.split("_")[1]
    
    if region_key in REGIONS_DATA:
        data = REGIONS_DATA[region_key]
        
        await callback.message.answer_photo(
            photo=data["photo"],
            caption=f"📌 **{data['title']}**\n\n{data['info']}\n\nQuyidagi tuman yoki shaharlardan birini tanlang:",
            reply_markup=get_districts_keyboard(region_key)
        )
    await callback.answer()

@dp.callback_query(F.data.startswith("tum_"))
async def district_selected(callback: CallbackQuery):
    # Callback ma'lumotidan viloyat va tuman nomini to'g'ri ajratib olish
    parts = callback.data.split("_", 2)
    region_key = parts[1]
    district_name = parts[2]
    
    if region_key in REGIONS_DATA and district_name in REGIONS_DATA[region_key]["districts"]:
        district_data = REGIONS_DATA[region_key]["districts"][district_name]
        region_title = REGIONS_DATA[region_key]["title"]
        
        back_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"⬅️ {region_title}ga qaytish", callback_data=f"vil_{region_key}")],
                [InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="back_to_main")]
            ]
        )
        
        await callback.message.answer_photo(
            photo=district_data["photo"],
            caption=f"📌 **{district_name}** ({region_title})\n\n{district_data['info']}",
            reply_markup=back_keyboard
        )
    await callback.answer()

@dp.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    await start_handler(callback.message)
    await callback.answer()


# Botni ishga tushirish
async def main():
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())