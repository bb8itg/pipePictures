import json
  
# Opening JSON file
f = open('pipe_json.json')
  
# returns JSON object as 
# a dictionary
a = '{"filename":}'
data = json.load(f)
  
# Iterating through the json
# list
classNumber = 1
for i in data:
    print(data[i]['filename'].split('.')[0])
    print(classNumber, data[i]['regions'][0]['shape_attributes']['x'], data[i]['regions'][0]['shape_attributes']['y'], data[i]['regions'][0]['shape_attributes']['width'], data[i]['regions'][0]['shape_attributes']['height'])
    f = open(("generatedAnnotation/"+data[i]['filename'].split('.')[0]+".txt"), "w")
    f.write(str(classNumber) + " " + str(data[i]['regions'][0]['shape_attributes']['x']) + " " + str(data[i]['regions'][0]['shape_attributes']['y']) + " " + str(data[i]['regions'][0]['shape_attributes']['width']) + " " + str(data[i]['regions'][0]['shape_attributes']['height']))
    f.close()
# Closing file
f.close()
