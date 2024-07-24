import json

def transform_item(item):
    add_agents = []
    if item["addSalmonella"]:
        add_agents.append(4)
    if item["addBrainKuru"]:
        add_agents.append(8)

    return {
        "itemClassname": item["itemClassname"],
        "setCount": [item["itemCount"], -1, -1],
        "chanceToSpawn": 1.0,
        "haveQuantity": item["haveQuantity"],
        "setQuantity": [item["countQuantity"], item["QuantRandMin"], item["QuantRandMax"]],
        "setHealth": [1, -1, -1],
        "toolHealthCoefEnable": 0,
        "coefHealthMinMaxValue": [0.5, 1.0],
        "toolQuantityCoefEnable": 0,
        "coefQuantityMinMaxValue": [0.5, 1.0],
        "toolDamageCoef": item["toolDamageCoef"],
        "addAgents": add_agents,
        "perkCoefEnable": item["perkCoefEnable"],
        "perkCoefList": [
            {
                "enableCoef": perk["enableCoef"],
                "perkID": perk["perkID"],
                "chanceToSpawn": 1.0,
                "setCount": [perk["setCount"], -1, -1],
                "haveQuantity": 1,
                "setQuantity": [perk["setQuantity"], item["QuantRandMin"], item["QuantRandMax"]],
                "setHealth": [1, -1, -1],
                "toolHealthCoefEnable": 0,
                "coefHealthMinMaxValue": [0.5, 1.0],
                "toolQuantityCoefEnable": 0,
                "coefQuantityMinMaxValue": [0.5, 1.0],
                "addAgents": add_agents
            } for perk in item.get("perkCoefList", [])
        ]
    }

def transform_data(data):
    return {
        "KillPoints": data["KillPoints"],
        "SkinningPoints": data["SkinningPoints"],
        "toolSkinDamageCoef": data["toolSkinDamageCoef"],
        "typeOfSkillKill": data["typeOfSkill"],
        "typeOfSkillSkinning": data["typeOfSkill"],
        "showNotify": 1,
        "modeKnifesAllow": 0,
        "allowknifesListKindOf": 1,
        "knifesList": [],
        "knifesListID": [],
        "ItemSkin": [transform_item(item) for item in data.get("ItemSkin", [])]
    }

def transform_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    transformed_data = {key: transform_data(value) for key, value in data.items()}

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(transformed_data, f, indent=4)

input_file = 'old.json'  # Укажите ваш файл с исходными данными
output_file = 'output.json'  # Укажите имя выходного файла

transform_file(input_file, output_file)
