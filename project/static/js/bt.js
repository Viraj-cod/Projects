gal_but = document.getElementsByClassName('gal')[0]

gal_but.addEventListener('mouseover',function(){
  gal_but.style.background = 'red';
})

gal_but.addEventListener('mouseout',function(){
  gal_but.style.background = '';
})

abt_but = document.getElementsByClassName('about')[0]

abt_but.addEventListener('mouseover',function(){
  abt_but.style.background = 'red';
})

abt_but.addEventListener('mouseout',function(){
  abt_but.style.background = '';
})

cnt_but = document.getElementsByClassName('cnt')[0]

cnt_but.addEventListener('mouseover',function(){
  cnt_but.style.background = 'red';
})

cnt_but.addEventListener('mouseout',function(){
  cnt_but.style.background = '';
})

prc_but = document.getElementsByClassName('price')[0]

prc_but.addEventListener('mouseover',function(){
  prc_but.style.background = 'red';
})

prc_but.addEventListener('mouseout',function(){
  prc_but.style.background = '';
})


//url("{% static 'img/bank.png' %}");

var firdi = "{% static 'img/edu.jpg' %}";
var secdi = "{% static 'img/grow.jpg' %}";
var therdi = "{% static 'img/sol.jpg' %}";

var dis = document.querySelector('.indisplay');
var images = [firdi, secdi, therdi]; // Store all the image URLs in an array
k = firdi

setInterval(()=>{
  if(k === firdi){
      dis.style.backgroundImage = firdi
      k = secdi
  }else if(k === secdi){
    dis.style.backgroundImage = secdi
    k = therdi
  }else if(k === therdi){
    dis.style.backgroundImage = therdi
    k = firdi
  }
},1000)



