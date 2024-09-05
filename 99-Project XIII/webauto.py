import webbrowser as wb

def web_auto():
    
    # Path of the chrome in your device
    chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
    
    URLS = (
        "facebook.com",
        "gmail.com",
        "github.com/sushanttwayana/"
    )
    
    for url in URLS :
        print("opening:" + url)
        wb.get(chrome_path).open(url)
        
web_auto()