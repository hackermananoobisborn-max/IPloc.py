#!/bin/python3
import socket
import http.client
import urllib.parse
import sys
import json
from datetime import datetime

if len(sys.argv) == 2 and sys.argv[1].find(".txt") != -1:
    try:
        store = open("apikey.txt", "r+")
        store.seek(0)
        if len(store.read()) < 32:
            API = input("input your ip2location API:")
            store.write(API)
            store.close()
            API = API
        else:
            store = open("apikey.txt", "r+")
            API = store.read()
        file = open(sys.argv[1], "r")
        for Host in file:
            Host = urllib.parse.urlparse(Host.strip())
            if Host[1] == "":
                Host = Host[2].strip()
            elif Host[1] != "":
                Host = Host[1].strip()
            Resolved = socket.gethostbyname(Host.strip())
            param = {
                "key": API.strip(),
                "ip": Resolved.strip(),
            }
            conn = http.client.HTTPConnection("api.ip2location.io", 80)
            req = conn.request("GET ", "/?" + urllib.parse.urlencode(param))
            resp_Object = conn.getresponse()
            string_Resp = resp_Object.read().decode("utf-8")
            Dict_Conv = json.loads(string_Resp)
            Lat = Dict_Conv.get("latitude")
            Lon = Dict_Conv.get("longitude")
            maps_link = f"https://www.google.com/maps/search/?api=1&query={Lat},{Lon}"
            print("-" * 50)
            print("Scanning Target:", Host + " = " + Resolved)
            print(f"MAP:{maps_link}")
            print("Start:" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            print("-" * 50)
            print("ip[=]" + Dict_Conv.get("ip"))
            print("country_code[=]" + Dict_Conv.get("country_code"))
            print("country_name[=]" + Dict_Conv.get("country_name"))
            print("region_name[=]" + Dict_Conv.get("region_name"))
            print("city_name[=]" + Dict_Conv.get("city_name"))
            print("latitude[=]" + str(Dict_Conv.get("latitude")))
            print("longitude[=]" + str(Dict_Conv.get("longitude")))
            print("zip_code[=]" + Dict_Conv.get("zip_code"))
            print("time_zone[=]" + Dict_Conv.get("time_zone"))
            print("asn[=]" + Dict_Conv.get("asn"))
            print("as[=]" + Dict_Conv.get("as"))
            print("Request Error[=]", Dict_Conv.get("error"))
            Log = open("Log.txt", "a")
            Time = "Scanned at:" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            Log.write(f"\n \n{Time} \n{Host}\n{Resolved}\n{maps_link}\n{string_Resp}")
            print("\n")
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print(
            "Couldn't connect to the server,Please check your Internet connections and Firewalls and insure the file to scan exists then try again ."
        )
        sys.exit()
    except Exception as e:
        print(f"Error {e}")
    except KeyboardInterrupt:
        print("\n")
        print("Quiting Program")
    finally:
        sys.exit("Thanks for using my Geolocator")
elif len(sys.argv) == 1:
    try:
        Host = urllib.parse.urlparse(input("Target:").strip())
        store = open("apikey.txt", "r+")
        store.seek(0)
        if len(store.read()) < 32:
            API = input("input your ip2location API:")
            store.write(API)
            store.close()
            API = API
        else:
            store = open("apikey.txt", "r+")
            API = store.read()
        if Host[1] == "":
            Host = Host[2]
        else:
            Host = Host[1]
        Resolved = socket.gethostbyname(Host.strip())

        param = {
            "key": API.strip(),
            "ip": Resolved.strip(),
        }
        conn = http.client.HTTPConnection("api.ip2location.io", 80)
        req = conn.request("GET ", "/?" + urllib.parse.urlencode(param))
        resp_Object = conn.getresponse()
        string_Resp = resp_Object.read().decode("utf-8")
        Dict_Conv = json.loads(string_Resp)
        Lat = Dict_Conv.get("latitude")
        Lon = Dict_Conv.get("longitude")
        maps_link = f"https://www.google.com/maps/search/?api=1&query={Lat},{Lon}"
        print("-" * 50)
        print("Scanning Target:", Host + " = " + Resolved)
        print(f"MAP:{maps_link}")
        print("Start:" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        print("-" * 50)
        print("ip[=] " + Dict_Conv.get("ip"))
        print("country_code[=] " + Dict_Conv.get("country_code"))
        print("country_name[=] " + Dict_Conv.get("country_name"))
        print("region_name[=] " + Dict_Conv.get("region_name"))
        print("city_name[=] " + Dict_Conv.get("city_name"))
        print("latitude[=] " + str(Dict_Conv.get("latitude")))
        print("longitude[=] " + str(Dict_Conv.get("longitude")))
        print("zip_code[=] " + Dict_Conv.get("zip_code"))
        print("time_zone[=] " + Dict_Conv.get("time_zone"))
        print("asn[=] " + Dict_Conv.get("asn"))
        print("as[=] " + Dict_Conv.get("as"))
        print("Request Error[=]", Dict_Conv.get("error"))
        Log = open("Log.txt", "a")
        Time = "Scanned at:" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        Log.write(f"\n \n{Time} \n{Host}\n{Resolved}\n{maps_link}\n{string_Resp}")
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print(
            "Couldn't connect to the server Please check your Internet connections and Firewalls then try again."
        )
        sys.exit()
    except Exception as e:
        print(f"Error {e}")
    except KeyboardInterrupt:
        print("\n")
        print("\nQuiting Program")

    finally:
        sys.exit("Thanks for using my Geolocator")
else:
    print(
        "Invalid amount of arguments or invalid file type Please input a <filetype.txt> to continue or a valid amount of arguments e.g IPLOC <file.txt>"
    )
