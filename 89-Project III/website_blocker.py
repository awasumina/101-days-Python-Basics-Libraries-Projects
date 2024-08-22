# always run as administrator to block the website
# run this code in cmd as administrator

import datetime 
import time

# time when the website blocking is disabled 
end_time = datetime.datetime(2023, 10, 16)

# sites to block
site_block = ["www.daraz.com", "www.wscubetech.com"]

host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"
 
while True :
    
    if datetime.datetime.now() < end_time :
        
        print("Start Blocking")
        
        with open(host_path, "r+") as host_file :
            
            content = host_file.read()
            
            for website in site_block :
                if website not in content :
                    host_file.write(redirect +" "+website+"\n")
                    
                else :
                    pass
    
    else :
        with open(host_path, "r+") as host_file :
            
            content = host_file.readlines()
            host_file.seek(0) # file pointer to the start
            
            for lines in content :
                
                if not any(website in lines for wesite in site_block):
                    host_file.write(lines)
                
            host_file.truncate()
        
        time.sleep(5)