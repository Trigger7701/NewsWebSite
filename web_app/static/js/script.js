function like(user_id,new_id) {
	url = '127.0.0.1:8000/like_dislike/'
	fetch(url,{
    method:'POST',
    headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({'user_id':user_id,'new_id':new_id})
    })
    .then((response)=>{
    console.log(response.json())
    })
    // .then((data)=>{
    // location.reload()
    // })

}	