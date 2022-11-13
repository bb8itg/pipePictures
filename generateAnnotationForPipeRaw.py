import json
  
# Opening JSON file
f = open('pipe_json.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
normalize = json.load(open('pipe_coco.json'))
# Iterating through the json
# list
widthHeightList = []
for i in normalize['images']:
    widthHeightList.append((i['width'],i['height'],i['file_name']))



classNumber = 81
for i in data:
    w = h = 0.0
    for j in widthHeightList:
        if j[2].split('.')[0] == data[i]['filename'].split('.')[0]:
            w = float(j[0])
            h = float(j[1])
    f = open(("generatedAnnotation/"+data[i]['filename'].split('.')[0]+".txt"), "w")
    f.write(str(classNumber) + " " + format(float(data[i]['regions'][0]['shape_attributes']['x'])/w, '.6f') + " " + format(float(data[i]['regions'][0]['shape_attributes']['y'])/h, '.6f') + " " + format(float(data[i]['regions'][0]['shape_attributes']['width'])/w, '.6f') + " " + format(float(data[i]['regions'][0]['shape_attributes']['height'])/h, '.6f'))
# Closing file
f.close()
