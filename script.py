import os,json

with open('jsonfile.json') as f:
	data = json.load(f)

obj = data["Dependencies"]


#for i in obj:
#	print(i+"=="+obj[i])
	
cmd = "pip install "
failed_cases = [];
for i in obj:
	try:
		return_status = os.system(cmd+i+"=="+obj[i])
		if return_status == 1:
			failed_cases.append(i+"=="+obj[i]);
	except:
		print("Exception occured while installing " , i+"=="+obj[i])
		failed_cases.append(i+"=="+obj[i]);

if len(failed_cases) > 0:
	print("The following packages were not installed.")
	for i in failed_cases:
		print(i)
else:
	print("Success")
