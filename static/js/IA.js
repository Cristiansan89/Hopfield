cargar = () => {
aiterar=grid.getElementsByTagName('div')
arr=[]
for(i in aiterar){

    console.log(aiterar[i])
    console.log(aiterar[i].className)
    if(aiterar[i].className=='color' ){
        arr.push(1)
    }else if(aiterar[i].className=='square'){
         arr.push(-1)
    }

}

url="http://127.0.0.1:8080/imagenes"
var a=1
var data={"imagen":arr}
	fetch(url, {
  method: 'POST', // or 'PUT'
  body: JSON.stringify(data), // data can be `string` or {object}!
  headers:{
    'Content-Type': 'application/json'
  }
    }).then(res => res.json())
    .then(response =>{

    })
}

analizar = () => {}