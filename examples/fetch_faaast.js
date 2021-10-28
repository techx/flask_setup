const endpoint = "http://0.0.0.0:5100/count/add/ani"

for(let i=0; i<5000; i++){
    fetch(endpoint)
    .then(()=>{
        console.log("Fetched");
    })
    .catch(console.error)
}

// more reasonable
for(let i=0; i<10; i++){
    fetch(endpoint)
    .then(()=>{
        console.log("Fetched");
    })
    .catch(console.error)
}

//one at a time
for(let i=0; i<5000; i++){
    await fetch(endpoint)
    .then(()=>{
        console.log("Fetched");
    })
    .catch(console.error)
}



q = []
//batched
for(let i=0; i<5000; i++){
    q.push(fetch(endpoint)
    .then(()=>{
        console.log("Fetched");
    })
    .catch(console.error));
    if(q.length==500){
        await Promise.all(q)
        q = []
    }
}