const content = document.querySelector("#content");
function sendRequest(){
    console.log("saving...");
    // TODO: Construct JSON and send it to the api
    
    // for (var block of content.children){
    //     for (var el of block.children){
    //     }
    // }
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
        "class": "title",
        "rows": 1,
    });
 
    content.appendChild(div);
    div.appendChild(title);
}

function paragrapghSpawn(){
    par = elelmentBuilder("textarea",
    {
        "class": "paragraph",
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