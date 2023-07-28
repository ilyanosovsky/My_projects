fetch('http://localhost:8000/books/all/',{
    method:'GET'
  })
  .then(res=>res.json())
  .then(data=>{
    console.log(data);
  })
  .catch(e => {
    console.log(e);
  })