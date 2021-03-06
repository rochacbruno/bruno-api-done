import time
sleep = time.sleep

def fazer_burger(senha, n):
    print(f"fazendo burger {n} para {senha}")
    sleep(2)
    return b" [|O] "


async def app(scope, receive, send):        
    await send({
        'type': 'http.response.start',
        'status': 200,
    })

    senha = scope.get("path", "0")
    burger1 = fazer_burger(senha, 1)
    burger2 = fazer_burger(senha, 2)
    burger3 = fazer_burger(senha, 3)
    body = senha.encode() + burger1 + burger2 + burger3
    
    await send({
        'type': 'http.response.body',
        'body': body,
    })
    print("request terminado")