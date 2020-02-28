function name(){
    let names =["Cody","James","Dave", "Mike","Ryan","Michael"];
    let randomName = names[Math.floor(Math.random() * names.length)];
    helloWorld(randomName);
};

function helloWorld(randomName){
        console.log(randomName);
};

name();
