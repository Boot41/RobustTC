

const CreateEmployer = ()=>{

    const handleCreateEmployer = ()=>{
        let url = 'http://0.0.0.0:8080/proxy/8000/api/employer/';
        let method = "POST";
        let payload = {
            name:"Amazon",
            email:"amazon@gmail.com"
        }
        let headers = {
            'Content-Type':'application/json'
        };

        fetch(url,{
            method,
            headers,
            body: JSON.stringify(payload)
        })
        .then((response)=> response.json())
        .then((response)=>{
            console.log("Response is :",response);
        })
        .catch((err)=>{
            alert("Something went wrong")
        })
    }

    return(
        <button onClick={handleCreateEmployer}>
            Create new Employer
        </button>
    )
}

export default CreateEmployer;
