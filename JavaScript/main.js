import BruteUtil from "./BruteForcer/brute.js"
import promptSync from "prompt-sync";
const prompt = promptSync({sigint:true});

const s_baseCharset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?";

const sleep = ms => new Promise(r => setTimeout(r, ms));

function choose(array) {
    let index = Math.floor(Math.random() * array.length);
    return array[index];
}

function GenerateTestPassword(length){
    let finalStr = "";
    for(let i=0;i<length;i++) {
        finalStr += choose(s_baseCharset)
    };
    return finalStr;
};

async function main(){
    let s_password = "";
    let choice = prompt("Generate Or Enter Password (g/e) >\n- % ");
    if("ge".includes(choice)){
        switch(choice){
            case "g":
                let pwLength = prompt("Enter Password Length >\n- % ");
                s_password = GenerateTestPassword(pwLength).toString();
                console.log("Generated Password Is : "+s_password+". Starting...");
                await sleep(3000);
                break;
            case "e":
                s_password = prompt("Enter Password To Attempt >\n- % ").toString();
                console.log("Your Password Is : "+s_password+". Starting...");
                await sleep(3000);
                break;
            default:
                main();
                break;
        };
    };
    new BruteUtil(s_password, s_baseCharset, true).Attempt();
};

main()