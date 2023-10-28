import React, { useState, useEffect } from "react";

import NationalPark from "./NationalPark";

function AllNationalParks() {

    const [nationalParkArr, setNationalParkArr] = useState([]);

    useEffect(() => {
        fetch("/national_parks")
            .then((resp) => resp.json())
            .then((data) => setNationalParkArr(data))
    }, [])

    let nationalParkArrToRender = []

    if (nationalParkArr.length > 0) {
        nationalParkArrToRender = nationalParkArr.map((nationalParkObj) => (
            <NationalPark
                key = { nationalParkObj.id }
                id = { nationalParkObj.id }
                name = { nationalParkObj.name }
                state = { nationalParkObj.state }
            />
        ))
    }

    return (
        <div>
            {nationalParkArr.length > 0 ? nationalParkArrToRender : null}
        </div>
    )
}

export default AllNationalParks;