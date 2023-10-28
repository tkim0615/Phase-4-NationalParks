import React, { useState, useEffect } from "react";

function NationalPark( {id, name, state} ) {

    function deletePark() {
        fetch(`/national_parks/${id}` , {
            method : "DELETE"
        })
    }

    return (
        <div onClick = { deletePark }>
            <h1>{ name }</h1>
            <h2>{ state }</h2>
        </div>
    )
}

export default NationalPark;