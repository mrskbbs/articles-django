const content = document.querySelector("#content");
function sendRequest(){
    let packet = [];
    let block_ind = 0;

    //Construct a JSON packet
    for (var block of content.children){
        packet.push([]);
        let el_ind = 0;

        for (var el of block.children){
            packet[block_ind].push({});
            packet[block_ind][el_ind]["type"] = el.getAttribute("class");
            packet[block_ind][el_ind]["content"] = el.value;
            el_ind++;
        }

        block_ind++;
    }

    //TODO: Send a request to api
}

function elelmentBuilder(name, params){
    let el = document.createElement(name);
    for (var key in params){
        el.setAttribute(key, params[key]);
    }
    return el;
}

function titleSpawn(){
    div = elelmentBuilder("div",
    {
        "class": "block",
    });

    title = elelmentBuilder("textarea",
    {
        "class": "h1",
        "rows": 1,
    });
 
    content.appendChild(div);
    div.appendChild(title);
}

function paragrapghSpawn(){
    par = elelmentBuilder("textarea",
    {
        "class": "p",
        "rows": 10,  
    });

    div.appendChild(par);
}

titleSpawn();

//TODO: Set interval to 10 seconds
setInterval(()=>{
    let isautosave = document.querySelector("#autosave").checked;
    if (isautosave){
        sendRequest();
    }
}, 1000);