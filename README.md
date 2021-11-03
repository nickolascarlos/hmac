# Hash Message Authentication Code (HMAC)
Implementação "hash-agnostic" de um gerador e autenticador de HMAC

Algoritmo escrito em conformidade com o descrito pelo artigo [Message Authentication using Hash Functions — The
HMAC Construction]<https://cseweb.ucsd.edu//~mihir/papers/hmac-cb.pdf>

## Esquema do algoritmo implementado

![Esquema HMAC](https://raw.githubusercontent.com/nickolascarlos/hmac/main/images/esquema_hmac.jpeg)

## Exemplo de uso

```python
from hmac import HMAC
import hashing

minha_chave = "minhachavesupersecreta"
minha_mensagem = "Mensagem de exemplo"

hmac_factory = HMAC(minha_chave, hashing.MD5) # Usará MD5 como função de hashing

# Gera o hash para minha_mensagem usando a chave minha_chave
msg_hash = hmac_factory.generate(minha_mensagem)

# Verifica se o conjunto (mensagem, hash) é válido (usando minha_chave)
hmac_factory.verify("Mensagem de exemplo", expected_hash=msg_hash) # Retorna True
hmac_factory.verify("Mensagem adulterada", expected_hash=msg_hash) # Retorna False
```