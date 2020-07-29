(async () => {
    let deviceBar = document.getElementById('deviceBar');
    let itemData;

    // * waits for the data to be resolved and return the value
    itemData = await loadData();

    // * presents data if the devices are clicked
    deviceBar.addEventListener('click', (e) => selectBrands(e));

    document.getElementById('search').addEventListener('input', (e) => search(itemData, e));

})();

function search(d, v) {
    v.preventDefault();
    v = v.target.value;

    let guide = ['iphone', 'iwatch', 'ipad', 'mac'];
    let bsClassDock = 'ml-lg-1 dock col-sm-11 col-md-5 col-lg-5';
    let bsClassH = 'text-rightorder-sm-2';
    let bsClassP = 'order-sm-1 my-auto';
    let docket = document.getElementById('docket');
    docket.innerHTML = "";

    guide.forEach(function (data) {
        d[data].forEach(function (newData) {
            if (newData.itemTitle != undefined && newData.itemTitle.toLowerCase().includes(v.toLowerCase())) {
                docket.insertAdjacentHTML('afterbegin', `
                        <section class="${bsClassDock}">
                            <h3 class="${bsClassH}">${newData.itemTitle}</h3>
                            <p class="${bsClassP}">${newData.itemPrice}</p>
                        </section>
                        `);
            }
        })
    })

    // for(i = 0; i < 3; i++){
    //     let c = 0;
    //     for(a = (d[guide[i]].length - 1); a > 0; --a) {
    //         if (d[guide[i]][c].itemTitle != undefined) {
    //             if (d[guide[i]][c].itemTitle.toLowerCase().includes(v.toLowerCase())) {
    //                 docket.insertAdjacentHTML('afterbegin',`
    //                     <section class="${bsClassDock}">
    //                         <h3 class="${bsClassH}">${d[guide[i]][c].itemTitle}</h3>
    //                         <p class="${bsClassP}">${d[guide[i]][c].itemPrice}</p>
    //                     </section>
    //                     `);
    //             }
    //         }
    //         if (d[guide[i]][a].itemTitle != undefined) {
    //             if (d[guide[i]][a].itemTitle.toLowerCase().includes(v.toLowerCase())) {
    //                 docket.insertAdjacentHTML('afterbegin',`
    //                     <section class="${bsClassDock}">
    //                         <h3 class="${bsClassH}">${d[guide[i]][a].itemTitle}</h3>
    //                         <p class="${bsClassP}">${d[guide[i]][a].itemPrice}</p>
    //                     </section>
    //                 `);
    //             }
    //         }
    //         c++;
    //     }
    // }
}

async function loadData() {
    let data = await fetch('https://cors-anywhere.herokuapp.com/' + 'https://www.parsehub.com/api/v2/runs/trkeTYEUyhGG/data?api_key=tDZO3OBEtm7b&format=json')
    .then(response => response.json())
    .then(thedata => {
        realData = thedata;
        return thedata;
    })
    .catch(err => {
        console.error(`Error: ${err}`);
    })
    return data;
}

function selectBrands(e) {
    let docket = document.getElementById('docket');
    let brand = e.target.innerText;
    let jsonLink = 'https://www.parsehub.com/api/v2/runs/trkeTYEUyhGG/data?api_key=tDZO3OBEtm7b&format=json';
    let prox = 'https://cors-anywhere.herokuapp.com/';

    let bsClassDock = 'ml-lg-1 dock col-sm-11 col-md-5 col-lg-5';
    let bsClassH = 'text-rightorder-sm-2';
    let bsClassP = 'order-sm-1 my-auto';

    docket.innerHTML = "";

    switch (brand.toLowerCase()) {
        case 'iphone':
            {
                console.info(`iphone selected`);
                fetch(prox + jsonLink)
                .then(response => response.json())
                .then(data => {
                    console.table(data.iphone);
                    for(let i = 0; i < data.iphone.length; i++) {
                        docket.insertAdjacentHTML('afterbegin',`
                        <section class="${bsClassDock}">
                            <h3 class="${bsClassH}">${data.iphone[i].itemTitle.match(/iPhone?.*/g)}</h3>
                            <p class="${bsClassP}">${data.iphone[i].itemPrice}</p>
                        </section>
                        `);
                    }
                    return data;
                })
                .catch(err => {
                    console.error(err);
                    return err;
                });

            }
            break;
        case 'ipad':
            {
                console.info(`ipad selected`);
                fetch(prox + jsonLink)
                .then(response => response.json())
                .then(data => {
                    for(let i = (data.ipad.length/2); i < data.ipad.length; i++){
                        docket.insertAdjacentHTML('afterbegin',`
                        <section class="${bsClassDock}">
                            <h3 class="${bsClassH}">${data.ipad[i].itemTitle.slice(0,110).match(/iPad?.*/g)}</h3>
                            <p>${data.ipad[i].itemPrice}</p>
                        </section>
                        `);
                    }
                    return data;
                })
                .catch(err => {
                    console.error(err);
                    return err;
                });
            }
            break;
        case 'iwatch':
            {
                console.info(`iwatch selected`);
                fetch(prox + jsonLink)
                .then(response => response.json())
                .then(data => {
                    for(let i = (data.iwatch.length/2); i < data.iwatch.length; i++){
                        docket.insertAdjacentHTML('afterbegin',`
                        <section class="${bsClassDock}">
                            <h3 class="${bsClassH}">${data.iwatch[i].itemTitle.slice(0,60).match(/iWatch?.*/g)}</h3>
                            <p>${data.iwatch[i].itemPrice}</p>
                        </section>
                        `);
                    }
                    return data;
                })
                .catch(err => {
                    console.error(err);
                    return err;
                });
            }
            break;
        case 'mac':
            {
                console.info(`mac selected`);
                fetch(prox + jsonLink)
                .then(response => response.json())
                .then(data => {
                    console.table(data.mac);
                    fetch(prox + jsonLink)
                .then(response => response.json())
                .then(data => {
                    for(let i = (data.mac.length/2); i < data.mac.length; i++){
                        docket.insertAdjacentHTML('afterbegin',`
                        <section class="${bsClassDock}">
                            <h3 class="${bsClassH}">${data.mac[i].itemTitle.slice(0,60).match(/A[0-3][0-9][0-9][0-9]?.*/g)}</h3>
                            <p>${data.mac[i].itemPrice}</p>
                        </section>
                        `);
                    }
                    return data;
                })
                .catch(err => {
                    console.error(err);
                    return err;
                });
                    return data;
                })
                .catch(err => {
                    console.error(err);
                    return err;
                });
            }
            break;
        default:
            {
                console.error(`something has gone really wrong lol`);
                console.error(e.target);
            }
            break;
    }
}