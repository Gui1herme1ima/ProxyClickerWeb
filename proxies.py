from queue import Queue
from threading import Lock

# Lista de proxies
proxies_list = [
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10001,
        "id": "Proxy 1"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10002,
        "id": "Proxy 2"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10003,
        "id": "Proxy 3"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10004,
        "id": "Proxy 4"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10005,
        "id": "Proxy 5"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10006,
        "id": "Proxy 6"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10007,
        "id": "Proxy 7"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10008,
        "id": "Proxy 8"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10009,
        "id": "Proxy 9"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10010,
        "id": "Proxy 10"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10011,
        "id": "Proxy 11"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10012,
        "id": "Proxy 12"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10013,
        "id": "Proxy 13"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10014,
        "id": "Proxy 14"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10015,
        "id": "Proxy 15"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10016,
        "id": "Proxy 16"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10017,
        "id": "Proxy 17"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10018,
        "id": "Proxy 18"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10019,
        "id": "Proxy 19"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10020,
        "id": "Proxy 20"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10021,
        "id": "Proxy 21"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10022,
        "id": "Proxy 22"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10023,
        "id": "Proxy 23"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10024,
        "id": "Proxy 24"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10025,
        "id": "Proxy 25"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10026,
        "id": "Proxy 26"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10027,
        "id": "Proxy 27"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10028,
        "id": "Proxy 28"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10029,
        "id": "Proxy 29"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10030,
        "id": "Proxy 30"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10031,
        "id": "Proxy 31"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10032,
        "id": "Proxy 32"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10033,
        "id": "Proxy 33"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10034,
        "id": "Proxy 34"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10035,
        "id": "Proxy 35"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10036,
        "id": "Proxy 36"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10037,
        "id": "Proxy 37"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10038,
        "id": "Proxy 38"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10039,
        "id": "Proxy 39"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10040,
        "id": "Proxy 40"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10041,
        "id": "Proxy 41"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10042,
        "id": "Proxy 42"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10043,
        "id": "Proxy 43"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10044,
        "id": "Proxy 44"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10045,
        "id": "Proxy 45"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10046,
        "id": "Proxy 46"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10047,
        "id": "Proxy 47"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10048,
        "id": "Proxy 48"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10049,
        "id": "Proxy 49"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.decodo.com",
        "porta": 10050,
        "id": "Proxy 50"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10051,
        "id": "Proxy 51"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10052,
        "id": "Proxy 52"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10053,
        "id": "Proxy 53"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10054,
        "id": "Proxy 54"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10055,
        "id": "Proxy 55"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10056,
        "id": "Proxy 56"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10057,
        "id": "Proxy 57"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10058,
        "id": "Proxy 58"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10059,
        "id": "Proxy 59"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10060,
        "id": "Proxy 60"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10061,
        "id": "Proxy 61"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10062,
        "id": "Proxy 62"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10063,
        "id": "Proxy 63"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10064,
        "id": "Proxy 64"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10065,
        "id": "Proxy 65"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10066,
        "id": "Proxy 66"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10067,
        "id": "Proxy 67"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10068,
        "id": "Proxy 68"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10069,
        "id": "Proxy 69"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10070,
        "id": "Proxy 70"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10071,
        "id": "Proxy 71"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10072,
        "id": "Proxy 72"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10073,
        "id": "Proxy 73"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10074,
        "id": "Proxy 74"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10075,
        "id": "Proxy 75"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10076,
        "id": "Proxy 76"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10077,
        "id": "Proxy 77"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10078,
        "id": "Proxy 78"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10079,
        "id": "Proxy 79"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10080,
        "id": "Proxy 80"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10081,
        "id": "Proxy 81"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10082,
        "id": "Proxy 82"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10083,
        "id": "Proxy 83"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10084,
        "id": "Proxy 84"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10085,
        "id": "Proxy 85"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10086,
        "id": "Proxy 86"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10087,
        "id": "Proxy 87"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10088,
        "id": "Proxy 88"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10089,
        "id": "Proxy 89"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10090,
        "id": "Proxy 90"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10091,
        "id": "Proxy 91"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10092,
        "id": "Proxy 92"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10093,
        "id": "Proxy 93"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10094,
        "id": "Proxy 94"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10095,
        "id": "Proxy 95"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10096,
        "id": "Proxy 96"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10097,
        "id": "Proxy 97"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10098,
        "id": "Proxy 98"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10099,
        "id": "Proxy 99"
    },
    {
        "usuario": "user-sp64heqxiv-sessionduration-1",
        "senha": "Nxa+pD4n2s8tUztUh7",
        "host": "br.smartproxy.com",
        "porta": 10100,
        "id": "Proxy 100"
    }
]

# Fila de proxies disponíveis
proxies_queue = Queue()

# Adiciona todas as proxies na fila
for proxy in proxies_list:
    proxies_queue.put(proxy)

# Lock para garantir que a alocação de proxies seja thread-safe
proxy_lock = Lock()
