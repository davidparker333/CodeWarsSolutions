// How do you create a private function in JS?


// JS doesn't natively have private functions, but you can use a closure to emulate that functionality

secretVar = () => {
    let private = "secrets in here";
    return () => {
        return private;
    }
}

let getPrivate = secretVar();

console.log(getPrivate());