import { Chart, CategoryScale, ArcElement } from "chart.js";
import { Doughnut } from "react-chartjs-2";

type Props = {
    percent: number;
    color: string;
};

function OverallPie({ percent, color }: Props) {
    Chart.register(CategoryScale, ArcElement);

    const data = {
        datasets: [
            {
                data: [percent, 100 - percent],
                backgroundColor: [color, "#000000"],
                borderWidth: [0, 0],
            },
        ],
    };

    return (
        <div className="relative">
            <Doughnut
                className="relative"
                data={data}
                options={{
                    plugins: {
                        legend: {
                            display: false, // Hide the legend
                        },
                    },
                }}
            ></Doughnut>
        </div>
    );
}

export default OverallPie;
