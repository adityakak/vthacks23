import Navbar from "../../components/Navbar";
import SharedPie from "./SharedPie";
import SecondSharedPie from "./SecondSharedPie";
import ThirdSharedPie from "./ThirdSharedPie";
import Footer from "../../components/Footer";
import Houses from "../../components/Houses";

function Results() {
    return (
        <div>
            <Navbar />
            <SharedPie title="Overall Rating" percent={70} color="#E6903F" />
            <div className="md:flex justify-evenly">
                <div className="relative mb-20">
                    <SecondSharedPie
                        title="Environment Rating"
                        percent={40}
                        color="	#008000"
                    />
                    <div className="absolute top-0 left-0 bg-white w-full h-full opacity-0 hover:opacity-100 transition-opacity duration-300 z-10">
                        <div>
                            <div>
                                <ThirdSharedPie
                                    title="School Rating"
                                    percent={40}
                                    color="#008000"
                                />
                            </div>
                            <div className="flex justify-evenly">
                                <ThirdSharedPie
                                    title="Library Rating"
                                    percent={40}
                                    color="#008000"
                                />
                                <ThirdSharedPie
                                    title="Center Rating"
                                    percent={40}
                                    color="#008000"
                                />
                            </div>
                        </div>
                    </div>
                </div>

                <div className="relative mb-20">
                    <SecondSharedPie
                        title="Education Rating"
                        percent={40}
                        color="#FFFF00"
                    />
                    <div className="absolute top-0 left-0 bg-white w-full h-full opacity-0 hover:opacity-100 transition-opacity duration-300 z-10">
                        <div>
                            <div>
                                <ThirdSharedPie
                                    title="Air Quality"
                                    percent={40}
                                    color="#FFFF00"
                                />
                            </div>
                            <div className="flex justify-evenly">
                                <ThirdSharedPie
                                    title="Solar Rating"
                                    percent={40}
                                    color="#FFFF00"
                                />
                                <ThirdSharedPie
                                    title="Charging Stations"
                                    percent={40}
                                    color="#FFFF00"
                                />
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div className="text-center text-white text-2xl my-24">
                Check out these houses!
            </div>

            <div className="flex justify-evenly mb-10">
                <Houses
                    placeNumber={1}
                    imageLink=""
                    address="4033 Royal Lytham Drive, Fairfax, VA, 22033"
                    homesLink=""
                />
            </div>

            <Footer />
        </div>
    );
}

export default Results;
