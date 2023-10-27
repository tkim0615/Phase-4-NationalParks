import React, { useState, useEffect } from "react";

function AllUsers() {

    const [userArr, setUserArr] = useState([]);

    useEffect(() => {
        fetch("/users")
            .then((resp) => resp.json())
            .then((data) => setUserArr(data))
    }, [])

    console.log(userArr)

    return (
        <div></div>
    )
}