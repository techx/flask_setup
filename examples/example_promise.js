// Explicit promise syntax

timeoutPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('300 ms have passed');
    }, 300);

    if(Math.random()<0.5){
        reject("Random Bug")
    }
});