function like(new_id,action) {
	url = '/like_dislike/'
	fetch(url,{
    method:'POST',
    headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({'new_id':new_id,'action':action})
    })
    .then((response)=>{
    response.json().then((data) => {
        console.log(data.like,data.dis_like)
        document.getElementById('idlike').innerHTML = data.like
        document.getElementById('iddislike').innerHTML = data.dis_like
       })
    })
    // .then((data)=>{
    // location.reload()
    // })

}


