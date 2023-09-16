import Navbar from "../../components/Navbar";
import Overall from "./overallPie";

const chartStyles = {
    // Apply your styles here, for example:
    width: "300px",
    height: "300px",
};

function Results() {
    return (
        <div>
            <Navbar />
            <div>
                <div className="md:flex justify-left p-[30px] min-w-[500px] relative">
                    <Overall />
                    <div className="mt-10 relative group">
                        <span className="text-white text-4xl bg-left-bottom bg-gradient-to-r from-orange-400 to-orange-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out italic mt-10">
                            Your Overall Rating
                        </span>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Results;
