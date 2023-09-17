import OverallPie from "./OverallPie";
import useMediaQuery from "../../hooks/useMediaQuery";

type Props = {
    title: string;
    percent: number;
    color: string;
};

function SecondSharedPie({ title, percent, color }: Props) {
    const isAboveMediumScreens: boolean = useMediaQuery("(min-width: 550px)"); // returns a bool val as per the custom hook we created that takes in a media query string
    // in this case that string is the min-width of 1060 so it will return true if the viewport size is greater than 1060px
    // media queries must have paranthesees around them

    return (
        <div>
            {isAboveMediumScreens && (
                <div className="mx-auto w-[400px] pb-20">
                    <div className="mt-10 relative group text-center">
                        <span className="text-white text-3xl bg-left-bottom bg-gradient-to-r from-orange-400 to-orange-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out italic">
                            {title}
                        </span>
                    </div>
                    <div className="mt-10 relative">
                        <OverallPie percent={percent} color={color} />
                        <div className="absolute top-0 left-0 text-white text-6xl w-full h-full flex justify-center items-center">
                            {percent}
                        </div>
                    </div>
                </div>
            )}
            {!isAboveMediumScreens && (
                <div className="mx-auto w-[200px] pb-72">
                    <div className="mt-10 relative group text-center mb-8">
                        <span className="text-white text-2xl bg-left-bottom bg-gradient-to-r from-orange-400 to-orange-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out italic mt-10">
                            {title}
                        </span>
                    </div>
                    <div className="relative">
                        <OverallPie percent={percent} color={color} />
                        <div className="absolute top-0 left-0 text-white text-4xl w-full h-full flex justify-center items-center">
                            {percent}
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}

export default SecondSharedPie;
