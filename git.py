import os , random

for i in range(30):
    d = str(i) + 'days ago'
    # rand = random.randrange(1, 12)
    rand = 7
    with open('test.txt','a') as file:
        file.write(d+'\n')
    os.system('git add test.txt')
    
    os.system('git commit --date=" 2022-'+str(rand)+'-'+d+'" -m 1')
os.system('git push -u origin main')
