import Navbar from "../../components/Navbar";
import SharedPie from "./SharedPie";

function Results() {
    return (
        <div>
            <Navbar />
            <SharedPie title="Overall Rating" percent={70} color="#E6903F" />
            <div className="md:flex justify-evenly">
                <SharedPie
                    title="Environment Rating"
                    percent={40}
                    color="	#008000"
                />
                <SharedPie
                    title="Education Rating"
                    percent={40}
                    color="#FFFF00"
                />
            </div>
        </div>
    );
}

export default Results;
