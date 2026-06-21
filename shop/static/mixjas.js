

window.addEventListener('load', () => {
    let q = document.getElementById("q");
    let val = q.innerHTML;
    let min = document.getElementById("decrease");

    if(val > 0) {
        min.style.display = "inline";
    }
    myButton = document.getElementById("addToCart");

    if (myButton != null)
        myButton.addEventListener('click', event => addToCart(event, myButton.dataset.pid));
    if(min != null)
        min.addEventListener('click', e => removeFromCart(e, min.dataset.pid))
})

function getCookie(n) {
    cookie = document.cookie.split('; ');
    for(x of cookie) {
        const [title, value] = x.split('=');
        if(title == n)
            return value;
    }
    return null;
}
function increase() {
    // use state?
    sel = document.getElementById("q");
    bt = document.getElementById("addToCart");

    let val = sel.innerHTML
    sel.innerHTML = ++val

    bt.innerHTML = "+";
    let min = document.getElementById("decrease");
    min.style.display = "inline";
}

function decrease() {
    // use state?
    sel = document.getElementById("q");
    let min = document.getElementById("decrease");

    let val = sel.innerHTML;
    sel.innerHTML = --val;
    if(val == 0) {
        min.style.display = "none";
        let addbt = document.getElementById("addToCart");
        addbt.innerHTML = "add to shopping cart";
    }

}

async function removeFromCart(e, pid) {
    csrf = getCookie('csrftoken');

    fetch("/cart/decrease", {
        headers: {'X-CSRFTOKEN': csrf, "Content_Type": "application/json"},
        method: "POST",
        body: pid
    })
    .then(r => {if(r.status == 200) decrease()})
}


async function addToCart(e, pid) {
    csrf = getCookie('csrftoken');

    fetch("/cart/add", { headers: {'X-CSRFTOKEN': csrf, "Content_Type": "application/json"}, 
        method: "POST", body: pid })
    .then(r => {if(r.status == 200) increase()})

}