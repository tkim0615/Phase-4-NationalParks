import React, { useState, useEffect } from "react";

function User() {

    const [userID, setUserID] = useState(1)

    useEffect(() => {
        fetch(`/users/${userID}`)
            .then((resp) => resp.json())
            .then((data) => console.log(data))
    }, [userID])

    return (
        <div>
            <input placeholder = "id" onChange = {(e) => selectID(e)} />
        </div>
    )
}