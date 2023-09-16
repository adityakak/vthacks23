import Navbar from "../../components/Navbar";
import Overall from "./overallPie";
import useMediaQuery from "../../hooks/useMediaQuery";

const chartStyles = {
    // Apply your styles here, for example:
    width: "300px",
    height: "300px",
};

function Results() {
    const isAboveMediumScreens: boolean = useMediaQuery("(min-width: 550px)"); // returns a bool val as per the custom hook we created that takes in a media query string
    // in this case that string is the min-width of 1060 so it will return true if the viewport size is greater than 1060px
    // media queries must have paranthesees around them

    return (
        <div>
            <Navbar />
            <div>
                {isAboveMediumScreens && (
                    <div className="w-[500px] mx-auto">
                        <div className="mt-10 relative group text-center mb-8">
                            <span className="text-white text-4xl bg-left-bottom bg-gradient-to-r from-orange-400 to-orange-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out italic mt-10">
                                Your Overall Rating
                            </span>
                        </div>
                        <div className="">
                            <Overall />
                        </div>
                    </div>
                )}
                {!isAboveMediumScreens && (
                    <div className="w-[300px] mx-auto">
                        <div className="mt-10 relative group text-center mb-8">
                            <span className="text-white text-4xl bg-left-bottom bg-gradient-to-r from-orange-400 to-orange-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out italic mt-10">
                                Your Overall Rating
                            </span>
                        </div>
                        <div className="">
                            <Overall />
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}

export default Results;
