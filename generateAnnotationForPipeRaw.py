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


train = open("pipeTrain.txt", "w")
valid = open("pipeVal.txt", "w")

trainNum = 80
validNum = 20

trainNumCur = 0
validNumCur = 0

classNumber = 0
for i in data:
    
    w = h = 0.0
    for j in widthHeightList:
        if j[2].split('.')[0] == data[i]['filename'].split('.')[0]:
            w = float(j[0])
            h = float(j[1])
    f = open(("labels/"+data[i]['filename'].split('.')[0]+".txt"), "w")
    f.write(str(classNumber) + " " +
            format((float(data[i]['regions'][0]['shape_attributes']['x']) + float(data[i]['regions'][0]['shape_attributes']['width'])/2.0)/w, '.6f') + " " +
            format((float(data[i]['regions'][0]['shape_attributes']['y']) + float(data[i]['regions'][0]['shape_attributes']['height'])/2.0)/h, '.6f') + " " +
            format(float(data[i]['regions'][0]['shape_attributes']['width'])/w, '.6f') + " " +
            format(float(data[i]['regions'][0]['shape_attributes']['height'])/h, '.6f'))
    trainNumCur += 1
    if(trainNumCur <= trainNum):
        train.write("./images/"+data[i]['filename']+"\n")
    else:
        validNumCur += 1
        if(validNumCur <= validNum):
            valid.write("./images/"+data[i]['filename']+"\n")

# Closing file
f.close()
train.close()
valid.close()
