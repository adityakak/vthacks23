import Navbar from "../../components/Navbar";
import Overall from "./overallPie";

const chartStyles = {
  // Apply your styles here, for example:
  width: '300px',
  height: '300px',
};

function Results() {
  return (
    <div>
      <Navbar />
      <div id="dashboard">
        <div
          id="overallPieDiv"
          className="flex justify-left p-[30px] h-[500px] relative"
        >
          <Overall />
          <div className="mt-10 relative group">
            <span className="text-white text-4xl italic">Your Overall Rating</span>
            <span className="absolute left-0 w-full h-1 bg-orange-400 transition-all duration-500 opacity-0 group-hover:opacity-100"></span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Results;
