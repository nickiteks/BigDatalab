import os
import pandas as pd

oldpwd = os.getcwd()

os.chdir('C:/Users/NULS/Desktop/xhtym/projects/BigDatalab/photos/1000+')        

files = os.listdir()

try:
    files.remove('.DS_Store')
except:
    pass

print(files)

# словарь для записи данных в dataframe
data = {
    'filename':[],
    'value':[]
}

for file in files:

    data['filename'].append(file)

    filename_splited = file[:-4].split('_')
    data['value'].append(float(f'{filename_splited[3]}.{filename_splited[4]}'))


frame = pd.DataFrame(data)

frame.to_csv('C:/Users/NULS/Desktop/xhtym/projects/BigDatalab/lab2Data.csv', mode='a',index=False)