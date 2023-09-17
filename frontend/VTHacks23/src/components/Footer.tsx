import VTHacksLogo from "../assets/hacksLogo.svg";
import { FaGithub, FaReact } from "react-icons/fa";
import {
    BiLogoTailwindCss,
    BiLogoTypescript,
    BiLogoPython,
} from "react-icons/bi";

function Footer() {
    return (
        <div className="md:flex text-white bg-orange-600 text-center md:text-left">
            <div className="basis-1/3">
                <div className="px-32 py-12 flex flex-col">
                    <span className="text-2xl text-white mb-2">
                        Powered by ...
                    </span>
                    <div className="flex gap-2 justify-center md:justify-start">
                        <a href="https://react.dev/" target="_blank">
                            <FaReact className="h-8 w-8" />
                        </a>
                        <a href="https://v2.tailwindcss.com/" target="_blank">
                            <BiLogoTailwindCss className="h-8 w-8" />
                        </a>
                        <a
                            href="https://www.typescriptlang.org/docs/"
                            target="_blank"
                        >
                            <BiLogoTypescript className="h-8 w-8" />
                        </a>
                        <a href="https://www.python.org/">
                            <BiLogoPython className="h-8 w-8" />
                        </a>
                    </div>
                </div>
            </div>
            <div className="basis-1/3 flex justify-center items-center flex-col bg-orange-600">
                <div className="flex flex-col items-center justify-center pb-10 md:pb-0">
                    <span className="text-white text-4xl mb-4">
                        {" "}
                        Check out our repo!{" "}
                    </span>
                    <div className="text-4xl">
                        <a
                            href="https://github.com/adityakak/vthacks23"
                            target="_blanks"
                        >
                            <FaGithub />{" "}
                        </a>
                    </div>
                </div>
            </div>
            <div className="basis-1/3 flex justify-center items-center bg-orange-600">
                <div className="md:pb-0 pb-10">
                    <img alt="vthacks" src={VTHacksLogo} width={250} />
                </div>
            </div>
        </div>
    );
}

export default Footer;
