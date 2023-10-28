import React, { useState, useEffect } from "react";

function NewUser() {

    const [userArr, setUserArr] = useState([]);

    function addNewUser(e) {
        e.preventDefault();

        let newUserObj = {
            "username" : e.target.username.value,
            "password" : e.target.password.value
        }

        fetch("/users", {
            method : "POST",
            headers : {
                "Content-type" : "application/json"
            },
            body : JSON.stringify(newUserObj)
        })
        .then((resp) => resp.json())
        .then((returnedUserObj) => console.log(returnedUserObj))
    }

    return (
        <div>
            <form onSubmit = { (e) => addNewUser(e) }>
                <input placeholder = "username" name = "username" />
                <input placeholder = "password" name = "password" />
                <input type = "submit" />
            </form>
        </div>
    )
}

export default NewUser;