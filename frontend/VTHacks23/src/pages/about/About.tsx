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

            <Divider />
            <Footer />
        </div>
    );
}

export default About;
