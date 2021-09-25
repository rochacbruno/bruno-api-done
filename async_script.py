import asyncio
sleep = asyncio.sleep

async def fazer_burger(senha, n):
    print(f"fazendo async burger {n} para {senha}")
    await sleep(2)
    return b" [|O] "


async def app(scope, receive, send):        
    await send({
        'type': 'http.response.start',
        'status': 200,
    })

    senha = scope.get("path", "0")
    burger1 = await fazer_burger(senha, 1)
    burger2 = await fazer_burger(senha, 2)
    burger3 = await fazer_burger(senha, 3)
    body = senha.encode() + burger1 + burger2 + burger3
    
    await send({
        'type': 'http.response.body',
        'body': body,
    })
    print("request async terminado")