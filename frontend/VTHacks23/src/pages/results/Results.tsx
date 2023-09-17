import Navbar from "../../components/Navbar";
import SharedPie from "./SharedPie";
import SecondSharedPie from "./SecondSharedPie";
import ThirdSharedPie from "./ThirdSharedPie";
import Footer from "../../components/Footer";
import Houses from "../../components/Houses";
import { useLocation } from "react-router";
import { useEffect, useState } from "react";

// interface ResultProps {
//     education: number[];
//     environment: number[];
//     photos: string;
// }

function Results() {
    const location = useLocation();
    const data = location.state;
    const [homeData, setHomeData] = useState([])
    useEffect(() => {
        const homeD = []
        for (let x = 0; x < 5; x++) {
            const obj = {
                address: data.address[x],
                photos: data.photos[x],
                homesLink: data.homeLinks[x],
                index: x + 1
            }

            homeD.push(obj)
        }

        setHomeData(homeD)
    }, [])
    
    console.log(data);
    return (
        <div>
            <Navbar />
            <SharedPie title="Overall Rating" percent={Math.floor((data.education[3] * 0.5 + data.environment[3] * 0.5) * 100)} color="#E6903F" />
            <div className="md:flex justify-evenly">
                <div className="relative mb-20">
                    <SecondSharedPie
                        title="Education Rating"
                        percent={Math.floor(data.education[3] * 100)}
                        color="	#008000"
                    />
                    <div className="absolute top-0 left-0 bg-white w-full h-full opacity-0 hover:opacity-100 transition-opacity duration-300 z-10">
                        <div>
                            <div>
                                <ThirdSharedPie
                                    title="School Rating"
                                    percent={Math.floor(data.education[1] * 100)}
                                    color="#008000"
                                />
                            </div>
                            <div className="flex justify-evenly">
                                <ThirdSharedPie
                                    title="Library Rating"
                                    percent={Math.floor(data.education[0] * 100)}
                                    color="#008000"
                                />
                                <ThirdSharedPie
                                    title="Center Rating"
                                    percent={Math.floor(data.education[2] * 100)}
                                    color="#008000"
                                />
                            </div>
                        </div>
                    </div>
                </div>

                <div className="relative mb-20">
                    <SecondSharedPie
                        title="Environment Rating"
                        percent={Math.floor(data.environment[3] * 100)}
                        color="#FFFF00"
                    />
                    <div className="absolute top-0 left-0 bg-white w-full h-full opacity-0 hover:opacity-100 transition-opacity duration-300 z-10">
                        <div>
                            <div>
                                <ThirdSharedPie
                                    title="Air Quality"
                                    percent={100 - Math.floor(data.environment[0] * 100)}
                                    color="#FFFF00"
                                />
                            </div>
                            <div className="flex justify-evenly">
                                <ThirdSharedPie
                                    title="Solar Rating"
                                    percent={Math.floor(data.environment[1] * 100)}
                                    color="#FFFF00"
                                />
                                <ThirdSharedPie
                                    title="Charging Stations"
                                    percent={Math.floor(data.environment[2] * 100)}
                                    color="#FFFF00"
                                />
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div className="text-center text-white text-6xl my-24">
                Check out these houses!
            </div>

            <div className="flex flex-wrap gap-8 justify-evenly mb-10">
            {homeData.map((house) => {
                return <Houses
                placeNumber={house.index}
                imageLink={house.photos}
                address={house.address}
                homesLink={house.homesLink}
                />
            }
            )}
                
            </div>

            <Footer />
        </div>
    );
}

export default Results;