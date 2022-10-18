function product(array, repeat) {
    let pools = [];
    for(let pool in array) {
        pools += pool * repeat;
    };
    let result = []
    for (let pool in pools) {
        for(let x in result) {
            for(let y in pool) {
                result += x+[y];
            };
        };
    };
    for(let prod in result){
        return prod;
    };
};

class BruteUtil {
    constructor(password, charset, verbose){
        // Checks Go Off When They Should'nt... Fix Soon?

        // if(!(password instanceof String))
        //     throw new TypeError("password must be a string");

        this.password = password;

        // if(!(charset instanceof String))
        //     throw new TypeError("charset must be a string");
            
        this.charset = charset;

        // if(!(verbose instanceof Boolean))
        //     throw new TypeError("verbose must be a boolean");
            
        this.verbose = verbose;

        this.start = Date.now();
        this.end = Date.now();
        this.cracked = false;
    };

    Attempt() {
        this.start = Date.now();
        let attempts = 0;
        for(let i=0;i<27;i++){
            for(let letter in product(Array(this.charset), i)){
                attempts += 1;
                let guess = "";
                guess += letter
                console.log(letter)
                if(this.verbose)
                    console.log(guess)
                if(guess == this.password){
                    this.end = Date.now();
                    let timeDif = this.end - this.start
                    console.log("Cracked Password "+self.password+" in "+attempts+" tries and "+timeDif+" seconds!")
                    this.cracked = True
                    this._exit()
                };
            };
        };
    };

    _exit(){
        throw "stop execution";
    };
};

export default BruteUtil;