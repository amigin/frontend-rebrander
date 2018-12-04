import requests
import sys
import os
import json


def GetFileExtention(file_name):
    extention = file_name.split('/')[-1]

    if '.' in extention:
        extention = extention.split('.')[-1]
        if len(extention) > 0:
            return extention

    return ""


def ShouldWeLocalizeThatFile(file_name):
    ext = GetFileExtention(file_name)
    for extToLocalize in extsToLocalize:
        if (ext == extToLocalize):
            return True

    return False


def Localize(file_name):
    f = open(file_name, 'r')
    text = f.read()

    # Add Here Localization Lines
    text = text.replace("%BrandName%", localizationInfo["BrandName"])

    text = text.replace("%CompanyUrl%", localizationInfo["CompanyUrl"])

    text = text.replace("%SupportEmail%", localizationInfo["SupportEmail"])

    text = text.replace("%GitHubUrl%", localizationInfo["GitHubUrl"])

    text = text.replace("%favicon16.png%", localizationInfo["favicon16.png"])

    text = text.replace("%favicon32.png%", localizationInfo["favicon32.png"])

    text = text.replace("%favicon16.ico%", localizationInfo["favicon16.ico"])

    text = text.replace("%safari-pinned-tab.svg%", localizationInfo["safari-pinned-tab.svg"])

    text = text.replace("%logo.ios.svg%", localizationInfo["logo.ios.svg"])

    text = text.replace("%logo.android.svg%", localizationInfo["logo.android.svg"])

    text = text.replace("%logo.svg%", localizationInfo["logo.svg"])

    text = text.replace("%logo.png%", localizationInfo["logo.png"])

    text = text.replace("%logo-white.svg%", localizationInfo["logo-white.svg"])

    text = text.replace("%apple-touch-icon.png%", localizationInfo["apple-touch-icon.png"])	
	
	text = text.replace("%Facebook%", localizationInfo["Facebook"])
	
	text = text.replace("%Twitter%", localizationInfo["Twitter"])
	
	text = text.replace("%Instagram%", localizationInfo["Instagram"])
	
	text = text.replace("%Youtube%", localizationInfo["Youtube"])
	
	text = text.replace("%Linkedin%", localizationInfo["Linkedin"])
	
	text = text.replace("%Reddit%", localizationInfo["Reddit"])
	
	text = text.replace("%Telegram%", localizationInfo["Telegram"])	
	
	text = text.replace("%Appstore%", localizationInfo["Appstore"])
	
	text = text.replace("%Googleplay%", localizationInfo["Googleplay"])
	
	text = text.replace("%AssetLogo.svg%", localizationInfo["AssetLogo.svg"])
	
	text = text.replace("%DomainName%", localizationInfo["DomainName"])	

    f.close()

    fw = open(file_name, 'w')
    fw.writelines(text)
    fw.close()


def ScanFoldes(current_folder):
    for folder in os.listdir(current_folder):
        sub_file = current_folder + "/" + folder

        if os.path.isdir(sub_file):
            ScanFoldes(sub_file)
        else:
            if os.path.isfile(sub_file):
                if ShouldWeLocalizeThatFile(sub_file):
                    Localize(sub_file)


def GetLocalizationInfo(url):
    r = requests.get(url)
    j = json.loads(r.content)
    result = {}

    for itm in j:
        name = str(itm["Name"])
        value = str(itm["Value"])
        result[name] = value

    return result


extsToLocalize = []
localizationInfo = {}

if len(sys.argv) < 4:
    print("Please specify arguments. 1. Folder to scan; 2. Files to rebrand: example html/htm/css/js http://url/all?company=Primelabs")
    print("Ex: python3 localize.py ~/git html/htm/css/js http://url/all?company=Primelabs")
else:
    extsToLocalize = sys.argv[2].split('/')
    localizationInfo = GetLocalizationInfo(sys.argv[3])
    ScanFoldes(sys.argv[1])
    print(localizationInfo['CompanyUrl'])
