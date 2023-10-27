import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import App from './components/App'

function Router() {

    return (
        <BrowserRouter>
            <App />
        </BrowserRouter>
    )
}

const root = ReactDOM.createRoot(document.querySelector('#root'))
root.render(<Router />)