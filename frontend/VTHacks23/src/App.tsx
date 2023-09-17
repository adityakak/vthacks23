import { Route, Routes } from "react-router";
import { BrowserRouter } from "react-router-dom";
import Home from "./pages/home/Home";
import Results from "./pages/results/Results";
import ContactUs from "./pages/contactus/ContactUs";

function App() {
    return (
        <BrowserRouter>
            <div>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/results" element={<Results />} />
                    <Route path="/contact-us" element={<ContactUs />} />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

/* Description:

-) __(Insert Name) provides a percent score for both the Educational Equity and the Environmental footprint of the address given
-) A best alternative house to the one that was searched is displayed along with many others nearby and their respective ratings
-) Pay attention to the averages in your area!
-) Click the listings to view them on Homes.com

*/
export default App;
