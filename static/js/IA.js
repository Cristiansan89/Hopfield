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
  letra = document.getElementById('varLetra')
  url="http://127.0.0.1:8080/imagenes"
  var data={"imagen":arr, "letra":letra.value}
	fetch(url, {
    method: 'POST', // or 'PUT'
    body: JSON.stringify(data), // data can be `string` or {object}!
    headers:{
      'Content-Type': 'application/json'
    }
  }).then(res => res.json())
  .then(response =>{
  })
  letra.value = ""
}


analizar = () => {
  aiterar = grid.getElementsByClassName('div')
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
  console.log('array', arr)
  url="http://127.0.0.1:8080/analizar"
  var data={"analizar":arr}
	fetch(url, {
    method: 'POST', // or 'PUT'
    body: JSON.stringify(data), // data can be `string` or {object}!
    headers:{
      'Content-Type': 'application/json'
    }
  }).then(res => res.json())
  .then(response =>{
    console.log(response)
  })
}

