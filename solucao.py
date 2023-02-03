'''
    PROBLEMA ESCOLHIDO
        
        Criar um programa que receba um valor e retorne o maior 
        número primo que o divide.
        
    IDEIA DE RESOLUÇÃO
        
        Para a resolução do problema, pensei na criação de duas 
        funções. A primeira, e_primo que indicaria se um valor é
        primo ou não, e a segunda que juntaria todos os divisores
        do número inserido e retornaria o maior primo dessa lista.
        
    DESCRIÇÃO DETALHADA
    
        f: e_primo(num)
        
            A função e_primo, tenta dividir o número recebido 
            pelo conjunto de valores menor ou igual a raiz 
            desse número. Caso encontre algum valor que o divida
            a função retorna False, indicando que não é um número
            primo. Escolhi este método, pois um número não primo
            é composto por dois valores, sendo eles, um valor M
            menor que a raiz multiplicado por um valor N maior
            que a raiz, ou ambos os valores serão a própria raiz.
            
        f: maior_primo(num)
        
            A função maior_primo, armazena todos os divisores de 
            um valor 'num', de forma que ele armazena os dois 
            valores que multiplicados resultam em 'num', e 
            retorna o maior número primo presente nesta lista.
'''

# função que recebe um valor e retorna True se for um número primo, caso contrário retorna False
def e_primo(num):
    
    divisor_teste = int(num**(1/2))
    
    while divisor_teste > 1:
        if num % divisor_teste == 0:
            return False
        divisor_teste -= 1
    return True

# função que recebe um valor e retorna o maior número primo que divide esse valor
def maior_primo(num):
    
    divisor_teste = int(num**(1/2))
    divisores = []
    
    while divisor_teste >= 1:
        if num % divisor_teste == 0:
            divisores.append(divisor_teste)
            divisores.insert(0,num/divisor_teste)
        divisor_teste -= 1
    
    for divisor in divisores:
        if e_primo(divisor):
            return divisor

if __name__ == '__main__':
    
    print("Insira um número inteiro e eu retornarei o maior número primo que o divide")
    valor = int(input())
    
    print(maior_primo(valor))
        
    
