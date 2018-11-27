import json

j = list()

for i in range(300):
    dic = {
        "name": "测试"+str(i),
        "type": "line",
        "symbol": "circle",
        "symbolSize": 4,
        "itemStyle": {
            "normal": {
                "color": "red",
                "borderColor": "red"
            }
        },
        "data": [
            23*i,
            82*i,
            91*i,
            34*i,
            90*i,
            30*i,
            10*i,
            20*i,
            82*i,
            91*i,
            34*i,
            90*i,
            30*i,
            10*i
        ]
    }
    j.append(dic)


with open("data.json", "w+") as fp:
    fp.write(json.dumps(j))