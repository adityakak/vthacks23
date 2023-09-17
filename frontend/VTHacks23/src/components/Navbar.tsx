import { Link, useLocation } from "react-router-dom";
import { kebabCase } from "lodash";
import { useState } from "react";
import Logo from "../assets/logoBlack.png";

import {
    Bars3Icon,
    XMarkIcon,
} from "@heroicons/react/24/solid"; /* imports the Bars3Icon and xMarkIcon from @heroicons module, utilizing the entire path */
import useMediaQuery from "../hooks/useMediaQuery";

function Navbar() {
    // storing current location path
    const location = useLocation();

    const [isMenuToggled, setMenuToggled] = useState<boolean>(false);
    const isAboveMediumScreens: boolean = useMediaQuery("(min-width: 1205px)"); // returns a bool val as per the custom hook we created that takes in a media query string
    // in this case that string is the min-width of 1060 so it will return true if the viewport size is greater than 1060px
    // media queries must have paranthesees around them

    // function that takes in heading
    const isHeadingActive = (heading: string) => {
        const convHeading = kebabCase(heading); // converts heading text to lowercase & adds hyphens in spaces
        const parts = location.pathname.split("/"); // splits the pathname tring wherever a / is detected
        const activeHeading = parts[1]; // accesses the heading portion of the address
        return convHeading === activeHeading; // returns true or false depending on if on that specific heading page
    };

    // styling for different components
    const linkStyles =
        "hover:text-red-200 transition duration-300 p-4 text-orange-400 "; // navbar menu items when hovered

    return (
        // div containing entire navbar (using flex for row view)
        <nav className="flex h-24 bg-white border-y-8 border-orange-400">
            {/* YIW + Logo (allocating 1/3 space for div, centered vertically) */}
            <div className="ml-4 mb-2 flex gap-3 items-center text-3xl font-bold">
                <Link to="/">
                    {" "}
                    <img alt="logo" src={Logo} width={250} />{" "}
                </Link>
            </div>

            {isAboveMediumScreens ? (
                <div className="flex items-center basis-4/5 justify-end font-bold">
                    {/* List of headers (flex for row view, gap between list items with margin on right) */}
                    <ul className="flex gap-12 mr-12">
                        {/* changing hover text color with a transition time of 300ms */}
                        <li>
                            <Link
                                className={`${linkStyles} ${
                                    isHeadingActive("About")
                                        ? "text-red-300"
                                        : ""
                                } `}
                                to="/about"
                            >
                                About
                            </Link>
                        </li>
                    </ul>
                </div>
            ) : (
                !isMenuToggled && (
                    // if min-width is less than 1060 then utilize this below (primarily for mobile devices)
                    <button
                        className="absolute top-5 right-6 rounded-full  p-2" // Rounded full makes it fully circular. padding of 2 all around
                        onClick={() => setMenuToggled(!isMenuToggled)} // When we click the icon, the menu will close or open depending on its previous state
                        type="button"
                    >
                        <Bars3Icon className="h-12 w-12 text-orange-400">
                            {" "}
                        </Bars3Icon>
                        {/* For an icon, you call it like this */}
                    </button>
                )
            )}

            {/* Mobile Menu */}
            {!isAboveMediumScreens && isMenuToggled && (
                <div className="fixed bottom-0 right-0 z-40 h-screen w-[300px] bg-orange-400 drop-shadow-xl">
                    {/* Exact Pixels in tailwind must be surrounded by [] */}
                    <div className="flex justify-end p-6">
                        <button
                            onClick={() => setMenuToggled(!isMenuToggled)}
                            type="button"
                        >
                            <XMarkIcon className="h-12 w-12 text-white" />{" "}
                            {/* XMarkIcon printed with button functionality */}
                        </button>
                    </div>

                    {/* Menu Items */}

                    <div className="ml-[15%] flex flex-col gap-8 text-xl text-white">
                        {/* Div for innerleft side of the right side of the div that will hold the links */}
                        {/* text will appear smaller than default font sizes and gap of 8 seperates each child element */}

                        <Link
                            className={`${
                                isHeadingActive("About") ? " text-white" : ""
                            } hover:text-red-300 transition duration-300`}
                            to="/about"
                        >
                            About
                        </Link>
                    </div>
                </div>
            )}
        </nav>
    );
}

// exporting the navbar
export default Navbar;
