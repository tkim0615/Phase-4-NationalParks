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

    function editExistingUser(e) {
        e.preventDefault();

        let editedUserObj = {
            "username" : e.target.username.value,
            "password" : e.target.password.value
        }

        fetch(`/users/${e.target.id.value}`, {
            method : "PATCH",
            headers : {
                "Content-type" : "application/json"
            },
            body : JSON.stringify(editedUserObj)
        })
        .then((resp) => resp.json())
        .then((returnedUserObj) => console.log(returnedUserObj))
    }

    return (
        <div>
            <div>
                <h2>Add New User</h2>
                <form onSubmit = { (e) => addNewUser(e) }>
                    <input placeholder = "username" name = "username" />
                    <input placeholder = "password" name = "password" />
                    <input type = "submit" />
                </form>
            </div>
            <div>
                <h2>Edit Existing User</h2>
                <form onSubmit = { (e) => editExistingUser(e) }>
                    <input placeholder = "id" name = "id" />
                    <input placeholder = "username" name = "username" />
                    <input placeholder = "password" name = "password" />
                    <input type = "submit" />
            </form>
        </div>
    </div>
    )
}

export default NewUser;