# Algoritmo escrito de acordo com <https://cseweb.ucsd.edu//~mihir/papers/hmac-cb.pdf>

import hashlib

# ENCODING: Usado na transformação da sequência de bytes em string para
# facilitar a operação de concatenação.
# Está sendo usado o latin1 pois ele não apresentou nenhum problema de conversão.
# Foram previamente testados ascii e utf8.

# TODO: Fazer a concatenação byte a byte para que o processo
# não fique refém de uma ENCODING, diminuindo, consequentemente,
# o risco de erros relacionados à codificação de strings.

ENCODING = 'latin1'

INNER = 1
OUTER = 2

# Funções HMAC

# Função para a geração do HMAC de uma mensagem
# params:
#   K = chave
#   Text = mensagem
#   H = função de hashing
def HMAC(K, Text, H):
    return H(xor_key(OUTER, K) + H(xor_key(INNER, K) + Text))

# Verifica a integridade e autenticidade de uma mensagem
def verify_HMAC(K, Text, H, hash):
    return HMAC(K, Text, H) == hash

# Funções auxiliares

# Função para facilitar o pré-processamento da chave
# Retorna a sequência de bytes codificados
def generate_key(key):
    return bytes(resize_key(key), "latin1")

# Retorna key acrescida de quantos 0's forem necessários
# para se completarem 64 caracteres, conforme especificado
# no artigo (no topo desse arquivo) em que esse trabalho se baseia
def resize_key(key):
        if len(key) > 64: raise Exception('key size must be less or equal to 64')
        number_of_zeros_to_append = 64 - len(key)
        return key + "0" * number_of_zeros_to_append

# Função para realizar o xor entre a chave e (ipad ou opad)
# params:
#   w = INNER | OUTER
#   key = chave
def xor_key(w, key):
    key = generate_key(key)
    base = 0x36 if w == INNER else (0x5C if w == OUTER else None)
    if not base: raise ValueError('Parameter w must be either INNER or OUTER')
    xored_key = []
    for byte in key:
        xored_key.append(byte ^ base)
    return bytes(xored_key).decode('latin1')