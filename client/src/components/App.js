import React from "react";
import { Routes, Route } from "react-router-dom";

import AllNationalParks from "./AllNationalParks";
import AllUsers from "./AllUsers";
import User from "./User";

function App() {

    return (
        <Routes>
            <Route path = '/users'>
                <Route index element = { <AllUsers /> } />
                <Route path = ':id' element = { <User /> } />
            </Route>
            <Route path = '/national_parks'>
                <Route index element = { <AllNationalParks /> } />
            </Route>
        </Routes>
    )
}

export default App;