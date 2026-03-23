import os
import re

TRANSLATE = {
    "應龍王": "YinglongKing",
    "夔龍王": "KuirongKing",
    "閃耀的": "Shining",
    "應龍霸王": "YinglongEmperor",
    "夔龍霸王": "KuirongEmperor",
    "盧德萊": "Rudra",
    "守衛者軍團長": "GuardianBG",
    "執政官軍團長": "ArchonBG",
    "被侵蝕的支配者": "ErodedDominator",
    "巨劍": "Greatsword",
    "長劍": "Sword",
    "短劍": "Dagger",
    "弓": "Bow",
    "魔法書": "Spellbook",
    "法珠": "Orb",
    "釘錘": "Mace",
    "法杖": "Staff",
    "臂甲": "Guarder",
    "絕滅刀": "Greatsword",
    "鱗片劍": "Sword",
    "腳爪": "Dagger",
    "絕命弓": "Bow",
    "禁書": "Spellbook",
    "深淵玉": "Orb",
    "滅錘": "Mace",
    "心臟": "Guarder",
    "捕食巨劍": "Greatsword",
    "灼熱劍": "Sword",
    "惡意": "Dagger",
    "灼熱弓": "Bow",
    "炎火": "Spellbook",
    "紅焰玉": "Orb",
    "赤熱錘": "Mace",
    "鎖鏈": "Guarder",
    "達人最上級提煉石": "MasterSupremeRefinerStone",
    "提煉的強固龍族角": "RefinedSolidBalaurHorn",
    "提煉的強結龍族角": "RefinedFirmBalaurHorn",
    "鞣製的強固龍族皮革": "TannedSolidBalaurLeather",
    "鞣製的強結龍族皮革": "TannedFirmBalaurLeather",
    "強化的強固龍族鱗片": "EnhancedSolidBalaurScale",
    "強化的強結龍族鱗片": "EnhancedFirmBalaurScale",
    "憤怒思念": "AngerThought",
    "憤怒意志": "AngerWill",
    "憤怒自我": "AngerSelf",
    "憤怒昇華": "AngerSublimation",
    "憤怒願望": "AngerDesire",
    "發狂的憤怒巫蠱": "CrazyAngerVoodoo",
    "發狂的憤怒心血": "CrazyAngerBlood",
    "強固的龍族皮革": "SolidBalaurLeather",
    "強固的龍族角": "SolidBalaurHorn",
    "強固的龍族鱗片": "SolidBalaurScale",
    "強結的龍族皮革": "FirmBalaurLeather",
    "強結的龍族角": "FirmBalaurHorn",
    "強結的龍族鱗片": "FirmBalaurScale",
    "(刻印)": "_Bind"
}

def translate_name(name):
    # Sort keys by length descending to match longest first
    keys = sorted(TRANSLATE.keys(), key=len, reverse=True)
    res = name
    for k in keys:
        res = res.replace(k, TRANSLATE[k])
    
    # Remove any remaining non-ascii or weird chars, just keep alphanumeric and underscore
    res = re.sub(r'[^a-zA-Z0-9_]', '', res)
    if not res:
        res = "item"
    return res

base_dir = r"c:\Users\EnosLo\Desktop\Antigravity\NC-AION2-Tools\git\nca2-craft-tool"
items_js_path = os.path.join(base_dir, "js", "items.js")

with open(items_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

image_paths = set(re.findall(r'"((?:nca2-craft-tool/)?images/[^"]+\.png)"', content))

count = 0
for old_path in image_paths:
    filename = old_path.split('/')[-1][:-4]
    new_filename = translate_name(filename) + ".png"
    new_path = "/".join(old_path.split('/')[:-1]) + "/" + new_filename
    
    # Rename on disk if exists
    abs_old = os.path.normpath(os.path.join(base_dir, old_path.replace('/', os.sep)))
    abs_new = os.path.normpath(os.path.join(base_dir, new_path.replace('/', os.sep)))
    
    if os.path.exists(abs_old) and abs_old != abs_new:
        try:
            os.rename(abs_old, abs_new)
            print(f"Renamed: {os.path.basename(abs_old)} -> {os.path.basename(abs_new)}")
        except Exception as e:
            print(f"Error renaming {abs_old}: {e}")
            
    # Update content
    content = content.replace(f'"{old_path}"', f'"{new_path}"')
    count += 1

with open(items_js_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated items.js, processed {count} image paths.")
