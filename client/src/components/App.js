import React from "react";
import { Routes, Route } from "react-router-dom";

import AllNationalParks from "./AllNationalParks";
import AllUsers from "./AllUsers";
import User from "./User";
import NewUser from "./NewUser";

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
            <Route path = '/add_new_user' element = { <NewUser /> } />
        </Routes>
    )
}

export default App;