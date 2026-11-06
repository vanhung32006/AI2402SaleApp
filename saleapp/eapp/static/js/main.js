function addToCart(id,name,price){
    fetch('/api/cart',{
        method: "post",
        body: JSON.stringify({
            "id" : id,
            "name" : name,
            "price" : price
        },
        headers: {
        'content-Type':'application/json'
        }
        }).then(res => res.json()}.then(data =>{
            console.info(data)
        })
        }

