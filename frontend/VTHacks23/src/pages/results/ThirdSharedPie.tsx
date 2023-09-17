import OverallPie from "./OverallPie";
import useMediaQuery from "../../hooks/useMediaQuery";

type Props = {
    title: string;
    percent: number;
    color: string;
};

function ThirdSharedPie({ title, percent, color }: Props) {
    const isAboveMediumScreens: boolean = useMediaQuery("(min-width: 550px)"); // returns a bool val as per the custom hook we created that takes in a media query string
    // in this case that string is the min-width of 1060 so it will return true if the viewport size is greater than 1060px
    // media queries must have paranthesees around them

    return (
        <div>
            {isAboveMediumScreens && (
                <div className="mx-auto w-[100px] pb-10">
                    <div className="mt-10 relative group text-center mb-8">
                        <span className="text-black text-2xl bg-left-bottom bg-gradient-to-r from-orange-400 to-orange-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out italic mt-10">
                            {title}
                        </span>
                    </div>
                    <div className="">
                        <OverallPie percent={percent} color={color} />
                    </div>
                </div>
            )}
            {!isAboveMediumScreens && (
                <div className="mx-auto w-[100px] pb-10">
                    <div className="mt-10 relative group text-center">
                        <span className="text-black text-2xl bg-left-bottom bg-gradient-to-r from-orange-400 to-orange-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out italic mt-10">
                            {title}
                        </span>
                    </div>
                    <div className="">
                        <OverallPie percent={percent} color={color} />
                    </div>
                </div>
            )}
        </div>
    );
}

export default ThirdSharedPie;
