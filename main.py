import ctypes
import string
import os
import time

USE_WEBHOOK = True

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


try: 
    from discord_webhook import DiscordWebhook 
except ImportError:  
    
    input(
        f"Module discord_webhook pas installé, pour installer faite '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nVous pouvez ignorer si vous n'utilisez pas de webhook.\nAppuyez entrée pour ignorer.")
    USE_WEBHOOK = False
try:  
    import requests  
except ImportError:  
    
    input(
        f"Module requests pas installé, pour installer faites '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nAppuyez sur entrée pour quitter")
    exit()  
try:  
    import numpy  
except ImportError:  
  
    input(
        f"Module numpy pas installé, pour installer faites '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nAppuyez sur entrée pour quitter")
    exit() 

# regarder si l'user est connecté à internet
url = "https://github.com"
try:
    response = requests.get(url)
    print("Internet check")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    input("Tu n'est pas connecté à internet.\nAppuyez sur entrée pour quitter")
    exit()  


class NitroGen:  
    def __init__(self): 
        self.fileName = "Nitro Codes.txt"  

    def main(self):  
        os.system('cls' if os.name == 'nt' else 'clear')  
        if os.name == "nt":  
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Générateur de nitro + checkeur | by Baal")  
        else:  
            print(f'\33]0;Générateur de nitro + checkeur | by Baal\a',
                  end='', flush=True) 

        print("""                                                               
BBBBBBBBBBBBBBBBB                                      lllllll 
B::::::::::::::::B                                     l:::::l 
B::::::BBBBBB:::::B                                    l:::::l 
BB:::::B     B:::::B                                   l:::::l 
  B::::B     B:::::B  aaaaaaaaaaaaa    aaaaaaaaaaaaa    l::::l 
  B::::B     B:::::B  a::::::::::::a   a::::::::::::a   l::::l 
  B::::BBBBBB:::::B   aaaaaaaaa:::::a  aaaaaaaaa:::::a  l::::l 
  B:::::::::::::BB             a::::a           a::::a  l::::l 
  B::::BBBBBB:::::B     aaaaaaa:::::a    aaaaaaa:::::a  l::::l 
  B::::B     B:::::B  aa::::::::::::a  aa::::::::::::a  l::::l 
  B::::B     B:::::B a::::aaaa::::::a a::::aaaa::::::a  l::::l 
  B::::B     B:::::Ba::::a    a:::::aa::::a    a:::::a  l::::l 
BB:::::BBBBBB::::::Ba::::a    a:::::aa::::a    a:::::a l::::::l
B:::::::::::::::::B a:::::aaaa::::::aa:::::aaaa::::::a l::::::l
B::::::::::::::::B   a::::::::::aa:::aa::::::::::aa:::al::::::l
BBBBBBBBBBBBBBBBB     aaaaaaaaaa  aaaa aaaaaaaaaa  aaaallllllll
                                                                """)
        time.sleep(2) 
  
        self.slowType("Créer par : BaalZephon#1533", .02)
        time.sleep(1)  
       
        self.slowType(
            "\nEntrer le nombre de nitro que vous voulez générer et check (recommandé 5000 ou plus): ", .02, newLine=False)

        try:
            num = int(input('')) 
        except ValueError:
            input("Numéro non spécifié\nAppuyez sur entrée pour quitter")
            exit()  

        if USE_WEBHOOK:
            
            self.slowType(
                "Si vous voulez utiliser un webhook discord, coller le ici ou appuyez sur entrée pour ignoré: ", .02, newLine=False)
            url = input('')  
        
            webhook = url if url != "" else None
            
            if webhook is not None:
                DiscordWebhook( 
                        url=url,
                        content=f"```Commencement\nJe vous enverrai les codes ici```"
                    ).execute()

       

        valid = []  
        invalid = 0  
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        
        c = numpy.random.choice(chars, size=[num, 23])
        for s in c:  
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"  

                result = self.quickChecker(url, webhook)  

                if result: 
                    
                    valid.append(url)
                else:  
                    invalid += 1 
            except KeyboardInterrupt:
             
                print("\nInterruption de l'utilisateur")
                break  

            except Exception as e:  
                print(f" Error | {url} ")  

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Générateur de nitro + checkeur - {len(valid)} Valide | {invalid} Invalide - Créer par BaalZephon#1533") 
                print("")
            else:  
               
                print(
                    f'\33]0;Générateur de nitro + checkeur - {len(valid)} Valide | {invalid} Invalide - Créer par BaalZephon#1533\a', end='', flush=True)

        print(f"""
Résultats:
 Valide: {len(valid)}
 Invalide: {invalid}
 Codes Valides: {', '.join(valid)}""") 

        
        input("\nC'est la fin , cliquez 5 fois sur entrée pour quitter")
        [input(i) for i in range(4, 0, -1)]  

  
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:  
            
            print(i, end="", flush=True)
            time.sleep(speed)  
        if newLine: 
            print() 
    def quickChecker(self, nitro:str, notify=None):  
      
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) 

        if response.status_code == 200:  
            
            print(f" Valid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:  
                
                file.write(nitro)

            if notify is not None: 
                DiscordWebhook(  
                    url=url,
                    content=f"Code nitro détécté! @everyone \n{nitro}"
                ).execute()

            return True  

    
        else:
           
            print(f" Invalide | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False  


if __name__ == '__main__':
    Gen = NitroGen()  
    Gen.main()  
