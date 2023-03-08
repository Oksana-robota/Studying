const myDiv = document.createElement('div');
myDiv.className = 'buttons';
myDiv.style.background = 'white';

['Add to friends', 'Write message', 'Job offer', 'Add HW'].map(buttonName => {
    let button = document.createElement('button');
    button.innerText = `${buttonName}`;
    button.style.cssText = 'margin-left: 65px; margin-bottom: 5px; border-radius: 10px; background-color: LightGrey;';
    myDiv.appendChild(button);
})

document.getElementsByTagName('body')[0].appendChild(myDiv);

const btn2 = document.getElementsByTagName('button')[1];
btn2.style.backgroundColor = 'Aquamarine';

let counter = Math.floor(Math.random() * 150);

const myAmnt = document.createElement('div');
myAmnt.className = 'counter';
myAmnt.style.background = 'white';
myAmnt.innerText = `Friends: ${counter}`;

document.getElementsByTagName('body')[0].appendChild(myAmnt);

const btn = document.getElementsByTagName('button')[0];


btn.addEventListener("click", (Btnevent) => {
    counter += 1;
    myAmnt.innerText = `Friends: ${counter}`
    btn.innerText = 'Waiting for confirmation';
    Btnevent.target.disabled = true;
    });

btn2.addEventListener("click", (Btnevent) => {
    btn2.style.backgroundColor = 'LightGrey';
})

const btn3 = document.getElementsByTagName('button')[2];
btn3.addEventListener("click", (Btnevent) => {
    btn.style.display = ((btn.style.display!='none') ? 'none' : 'block');
    })

const btn4 = document.getElementsByTagName('button')[3];
btn4.addEventListener("click", (Btnevent) => {

    let tbrow = document.createElement('tr');
    let tbcol1 = document.createElement("td");
    tbcol1.innerHTML = "25";
    let tbcol2 = document.createElement("td");
    tbcol2.innerHTML = "Базова робота з HTML/CSS";
    let tbcol3 = document.createElement("td");
    tbcol3.innerHTML = "5<span>/5</span>";

    let tbel = document.getElementsByTagName('tbody')[0];
    tbrow.appendChild(tbcol1);
    tbrow.appendChild(tbcol2);
    tbrow.appendChild(tbcol3);
    tbel.insertBefore(tbrow, tbel.lastElementChild);
    document.getElementById('ttl').innerHTML = '75/<span>75</span>';
    })