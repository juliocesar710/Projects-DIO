print ("testando...")

import speech_recognition as sr

import os


#Função responsável por ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone para ouvir o usuário
    microfone = sr.Recognizer()

    #usando o microfone
    with sr.Microphone() as source:
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Avisa o usuário que está pronto para ouvir
        print("Diga alguma coisa: ")
        
        #Armazena a informacao de audio na variavel
        audio = microfone.listen(source)

    try:
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language='pt-BR')

        if "navegador" in frase:
            os.system("start opera.exe")
            return False
        
        elif "jogar" in frase:
            os.system(r'"C:\Program Files (x86)\Steam\Steam.exe"')
            return False
        
        elif "conversar" in frase:
            os.system(r'"C:\Users\julio\AppData\Local\Discord\Update.exe --processStart Discord.exe"')
            return False
        
        elif "pronto" in frase:
            os.system(r'"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"')
            return False
        
        elif "ouvir" in frase:
            os.system(r'"C:\Users\julio\AppData\Roaming\Spotify\Spotify.exe"')
            return False

        elif "fechar" in frase:
            print("Encerrando o programa...")
            return True
    
        #Retorna a frase pronunciada
        print("Você disse: " + frase)
    
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
    
    return False
    
while True:
    if ouvir_microfone():
        break