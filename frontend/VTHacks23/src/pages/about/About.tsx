import Navbar from "../../components/Navbar";
import Footer from "../../components/Footer";
import DeveloperCard from "../../components/DeveloperCard";
import { developers } from "./develop";
import Divider from "../../components/Divider";

function About() {
    return (
        <div>
            <Navbar />
            <div className="text-white italic text-6xl flex justify-center py-24">
                Meet the Developers
            </div>

            <div className="flex flex-wrap gap-16 pb-16 py-8 justify-center">
                {developers.map((developer) => (
                    <DeveloperCard
                        key={developer.id}
                        name={developer.name}
                        image={developer.image}
                    />
                ))}
            </div>
            <div className="my-10">
                <Divider />
            </div>
            <div className="text-white text-4xl leading-relaxed w-3/4 mx-auto my-10">
                Description:

                ScoreMyHome provides a percent score for both the Educational Equity and the Environmental footprint of the address given
                 A best alternative house to the one that was searched is displayed along with many others nearby and their respective ratings
                Pay attention to the averages in your area!
                Click the listings to view them on Homes.com
            </div>
            

            <Footer />
        </div>
    );
}

export default About;
